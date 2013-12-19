#!/usr/bin/python

import cli.app

class YAML2TimelineHTMLRenderer:
    'The main class to render a YAML document into HTML timeline.'
    TEMPLATE_HEADER = u'''
<html>
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="30">
  <meta name="viewport" content="width=device-width" />
  <title>Timeline</title>
  <style type="text/css" media="screen">
    body {
      margin:10px;
      padding:0;
      font-family: "HelveticaNeue-Light", Helvetica, Arial, sans-serif;
    }
    h1 {
      font-family: "HelveticaNeue-UltraLight", Helvetica, Arial, sans-serif;
      font-weight: normal;
      font-size: 20pt;
    }
  </style>
  <script type="text/javascript" src="https://www.google.com/jsapi?autoload={'modules':[{'name':'visualization', 'version':'1','packages':['timeline']}]}"></script>
  <script type="text/javascript">
  google.setOnLoadCallback(drawChart);
  function drawChart() {
    var container = document.getElementById('timeline');
    var chart = new google.visualization.Timeline(container);
    var dataTable = new google.visualization.DataTable();
    dataTable.addColumn({ type: 'string', id: 'Team' });
    dataTable.addColumn({ type: 'string', id: 'Task' });
    dataTable.addColumn({ type: 'date', id: 'Start' });
    dataTable.addColumn({ type: 'date', id: 'End' });
    dataTable.addRows([
      ['Today', 'Today', new Date(), new Date()],'''
    TEMPLATE_FOOTER = u'''
  ]);
  var options = {
    timeline: {
      colorByRowLabel: true,
      barLabelStyle: {fontSize:10}
    }
  };
  chart.draw(dataTable, options);
}
</script>
</head>
<body>
<h1>Timeline</h1>
<div id="timeline" style="width: 100%; height: 100%"></div>
</body>
</html>'''

    def __init__(self, input_file):
        import yaml
        with open(input_file, 'r') as f:
            self.model = yaml.load(f.read())
            assert isinstance(self.model, dict)

    def output_to_file(self, output_file):
        def py_datetime_to_js(py_datetime):
            if py_datetime == None:
                return ''
            try:
                return 'new Date(%d, %d, %d, %d, %d, %d)' % \
                    (py_datetime.year, py_datetime.month - 1,
                     py_datetime.day, py_datetime.hour,
                     py_datetime.min, py_datetime.second)
            except:
                return u'new Date(%d, %d, %d)' % \
                    (py_datetime.year, py_datetime.month - 1,
                     py_datetime.day)

        rows = ''
        for key in self.model:
            items = self.model[key]
            for item in items:
                row = u'\n      ["%s", "%s", %s, %s],' % \
                      (key, item['title'],
                       py_datetime_to_js(item['begin']),
                       py_datetime_to_js(item['end']))
                rows += row
                html = YAML2TimelineHTMLRenderer.TEMPLATE_HEADER + rows +\
                       YAML2TimelineHTMLRenderer.TEMPLATE_FOOTER
        with open(output_file, 'w') as f:
            f.write(html)

@cli.app.CommandLineApp
def yaml2timeline(app):
    input_file = app.params.input_file
    output_file = app.params.output_file
    YAML2TimelineHTMLRenderer(input_file).output_to_file(output_file)

yaml2timeline.add_param("input_file", help="input file", default=1, type=str)
yaml2timeline.add_param("output_file", help="output file", default=1, type=str)

def main():
    yaml2timeline.run()

if __name__ == "__main__":
    main()
