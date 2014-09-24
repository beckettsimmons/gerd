import default_templates

class Database():
    """ Our object for creating ERD database-like dot code. """
    def __init__(self, tables):
        self.tables = tables
        self.dot = ""

    def create_tables(self):
        """ Creates the dot code for tables in self.tables. """
        for table in self.tables:
            self.dot += table.dot

    def get_table(self, table_name):
        """ Gets a table in self.tables based on name. """
        i = 0
        for table in self.tables:
            if table.name == table_name:
                return i
            i += 1
        return -1

    def create_connections(self):
        """ Creates the foreign-key connections between tables. """
        for table in self.tables:
            if table.foreign_keys != None:
                for local_field_name, foreign_table_name, foreign_field_name\
                        in table.foreign_keys:

                    foreign_table_index = self.get_table(foreign_table_name)
                    if foreign_table_index == -1:
                        print(
                            "Failed to create connection {connection}." +
                            "Invalid foreign table name."
                        ).format(
                            connection=(
                                local_field_name,
                                foreign_table_name,
                                foreign_field_name
                            )
                        )
                        continue

                    port_number = self.tables[foreign_table_index]\
                        .get_field_index(
                            foreign_field_name
                        )
                    if port_number == -1:
                        print(
                            "Failed to create connection {field_name}." +
                            "Invalid foreign table field name."
                        ).format(field_name=foreign_field_name)
                        continue

                    local_field_index = table.get_field_index(
                        local_field_name
                    )
                    self.dot +=(
                        table.name + ":" + str(local_field_index) +
                        " -> " +
                        foreign_table_name + ":" + str(port_number) + ";"
                    )

    def create_dot(self):
        """ Creates the database-like dot code. """
        self.dot = ""
        self.dot += default_templates.database_header_template
        self.create_tables()
        self.create_connections()
        self.dot += default_templates.database_footer_template
