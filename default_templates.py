""" Default templates that are to be used for creating dot code. """


database_header_template = """
digraph models_diagram{
  graph[
      overlap=false,
      ranksep=2,
      nodesep=1,
      splines=spline,
  ];
  node [shape=record, fontsize=9, fontname="Verdana"];
"""

table_header_template = """
  {table_name} [
    shape=none,
    margin=0,
    label=<
      <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
"""

table_nick_row_template = """
          <tr><td bgcolor="lightblue">{table_nick}</td></tr>
"""

table_row_template = """
          <tr><td port="{port_number}" align="left">{row_name}</td></tr>
"""

table_footer_template = """
      </table>
    >
  ];
"""

database_footer_template = """
}
"""
