from django.shortcuts import render
from chartapp.views import LineView, DonutView

from demoapp.models import LineModel, DonutModel
from demoapp.forms import LineForm, DonutForm


class LineChartView(LineView):
    model = LineModel
    form = LineForm

class DonutChartView(DonutView):
    model = DonutModel
    form = DonutForm
