from files_03_Document_Management.category import Category
from files_03_Document_Management.topic import Topic
from files_03_Document_Management.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__get_obj_by_id(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__get_obj_by_id(self.topics, topic_id)

        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__get_obj_by_id(self.documents, document_id)

        document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category = self.__get_obj_by_id(self.categories, category_id)

        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self.__get_obj_by_id(self.topics, topic_id)

        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self.__get_obj_by_id(self.documents, document_id)

        self.documents.remove(document)

    def get_document(self, document_id): # ?
        return self.__get_obj_by_id(self.documents, document_id)

    def __get_obj_by_id(self, list_of_objects, id):
        for category in list_of_objects:
            if category.id == id:
                return category

    def __repr__(self):
        return "\n".join([str(doc) for doc in self.documents])