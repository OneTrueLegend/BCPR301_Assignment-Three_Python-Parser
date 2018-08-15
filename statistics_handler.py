import sql

#By Jake Reddock
class ClassData:
    def __init__(self, class_name, attribute_count, method_count):
        self.class_name = class_name
        self.attribute_count = attribute_count
        self.method_count = method_count

#By Jake Reddock
class StatisticsHandler:
    def __init__(self):
        self.db = sql.database("example")

    def create_tables(self):
        self.db.query("CREATE TABLE IF NOT EXISTS ClassData ("
                      "classID INTEGER NOT NULL AUTO_INCREMENT "
                      "className VARCHAR(255)"
                      "attributeCount INTEGER "
                      "methodCount INTEGER"
                      ")")

    def insert_class(self, class_name, attribute_count, method_count):
        self.db.query("INSERT INTO ClassData VALUES('" +
                      class_name + "','" +
                      attribute_count + "','" +
                      method_count + "');")

    def get_class_data(self):
        class_data_list = []
        result = self.db.query("SELECT className,attributeCount,methodCount").fetch()
        for row in result:
            class_name = row['className']
            attribute_count = row['attributeCount']
            method_count = row['methodCount']
            class_data_list.append(ClassData(class_name, attribute_count, method_count))
        return class_data_list
