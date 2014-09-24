import default_templates

class Table():
    """ Our object for creating database table-like dot code. """

    def __init__(self, name, nick_name, fields, foreign_keys=None):
        self.fields = fields
        self.name = name
        # nick_name is the userfriendly name.
        self.nick_name = nick_name
        self.dot = ""
        self.foreign_keys = foreign_keys

        # Since the table is so simple, just create the dot on the spot.
        self.create_dot()

    # TODO: Make the port number independent of array position.
    def create_dot(self):
        """ Actually creates the ERD table like dot code. """
        self.dot += default_templates.table_header_template.format(
            table_name=self.name
        )
        self.dot += default_templates.table_nick_row_template.format(
            table_nick=self.nick_name
        )

        i = 0
        for column in self.fields:
            self.dot += default_templates.table_row_template.format(
                port_number = i,
                row_name = column
            )
            i += 1

        self.dot += default_templates.table_footer_template

    def get_field_index(self, field_name):
        """ Returns the index (port number) of a field based on name. """
        i = 0
        for field in self.fields:
            if field == field_name:
                return i
            i += 1
        return -1
