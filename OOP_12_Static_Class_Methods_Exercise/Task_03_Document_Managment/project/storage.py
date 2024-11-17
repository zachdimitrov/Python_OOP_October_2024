from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def find_in_list(search_id, lst):
        return next((x for x in lst if x.id == search_id), None)

    def edit_category(self, category_id: int, new_name: str):
        cat = self.find_in_list(category_id, self.categories)
        cat.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_in_list(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        doc = self.find_in_list(document_id, self.documents)
        doc.file_name = new_file_name

    def delete_category(self, category_id):
        cat = self.find_in_list(category_id, self.categories)
        self.categories.remove(cat)

    def delete_topic(self, topic_id):
        topic = self.find_in_list(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        doc = self.find_in_list(document_id, self.documents)
        self.documents.remove(doc)

    def get_document(self, document_id):
        return self.find_in_list(document_id, self.documents)

    def __repr__(self):
        return "\n".join([str(x) for x in self.documents])
