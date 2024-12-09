from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    VALID_TYPES = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}
    VALID_COLLECTORS = {"Museum": Museum, "PrivateCollector": PrivateCollector}

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.VALID_TYPES.keys():
            raise ValueError("Unknown artifact type!")
        if artifact_name in [a.name for a in self.artifacts]:
            raise ValueError(f"{artifact_name} has been already registered!")
        new_artifact = self.VALID_TYPES[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.VALID_COLLECTORS.keys():
            raise ValueError("Unknown collector type!")
        if collector_name in [a.name for a in self.collectors]:
            raise ValueError(f"{collector_name} has been already registered!")
        new_collector = self.VALID_COLLECTORS[collector_type](collector_name)
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector: BaseCollector = self.check_existence(collector_name, self.collectors)
        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact: BaseArtifact = self.check_existence(artifact_name, self.artifacts)
        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    @staticmethod
    def check_existence(name, collection):
        for obj in collection:
            if obj.name == name:
                return obj
        return None

    def remove_artifact(self, artifact_name: str):
        artifact: BaseArtifact = self.check_existence(artifact_name, self.artifacts)
        if not artifact:
            return f"No such artifact."
        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        count = 0
        for c in self.collectors:
            if c.available_money <= max_money:
                c.increase_money()
                count += 1
        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        collectors = sorted(self.collectors, key=lambda x: (-len(x.purchased_artifacts), x.name))
        result = "**Auction statistics**\n"
        result += f"Total number of sold artifacts: {sum([len(x.purchased_artifacts) for x in self.collectors])}\n"
        result += f"Available artifacts for sale: {len(self.artifacts)}\n"
        result += "***\n"
        for collector in collectors:
            result += f"{str(collector)}\n"

        return result.strip()
