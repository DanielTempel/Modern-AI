"""Rebuild the vector chart from the four model sizes supplied by the author."""
from pathlib import Path

from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT = Path(__file__).resolve().parent
FONT_DIR = Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('ChartArial', str(FONT_DIR / 'arial.ttf')))
pdfmetrics.registerFont(TTFont('ChartArialBold', str(FONT_DIR / 'arialbd.ttf')))
# Bottom-to-top order in ReportLab; PDF reads F16, Q8_0, Q4_K_M, Q2_K.
LABELS = ['Q2_K', 'Q4_K_M', 'Q8_0', 'F16']
SIZES_GIB = [2.95, 4.58, 7.95, 14.96]

drawing = Drawing(480, 164)
drawing.add(String(82, 146, 'Approximate model size',
                   fontName='ChartArialBold', fontSize=13,
                   fillColor=HexColor('#142E48')))
chart = HorizontalBarChart()
chart.x, chart.y, chart.width, chart.height = 82, 24, 337, 112
chart.data = [SIZES_GIB]
chart.categoryAxis.categoryNames = LABELS
chart.categoryAxis.labels.fontName = 'ChartArial'
chart.categoryAxis.labels.fontSize = 11
chart.categoryAxis.labels.dx = -8
chart.categoryAxis.visibleTicks = False
chart.categoryAxis.visibleAxis = False
chart.valueAxis.valueMin = 0
chart.valueAxis.valueMax = 16
chart.valueAxis.valueStep = 4
chart.valueAxis.labels.fontSize = 9
chart.valueAxis.labels.fontName = 'ChartArial'
chart.valueAxis.strokeColor = HexColor('#AFBAC4')
chart.valueAxis.labels.fillColor = HexColor('#536575')
chart.bars[0].fillColor = HexColor('#315E89')
chart.bars[0].strokeColor = None
chart.barWidth = 14
chart.groupSpacing = 8
chart.barLabelFormat = '%.2f GiB'
chart.barLabels.fontName = 'ChartArial'
chart.barLabels.fontSize = 10
chart.barLabels.boxAnchor = 'w'
chart.barLabels.dx = 5
chart.barLabels.fillColor = HexColor('#142E48')
drawing.add(chart)
renderPDF.drawToFile(drawing, str(OUTPUT / 'model-size-comparison.pdf'))
print('Created images/model-size-comparison.pdf')
