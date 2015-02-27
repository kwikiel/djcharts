import random
import string

from django.shortcuts import render
from django.views.generic.base import TemplateView


class ModelMissing(Exception):
    def __str__(self):
        return "Model not properly configured, please define model"


def random_string(prefix=''):
    """
    :param prefix: string prefix for random string
    :returns: generated string
    generate random string will be used for generating css id
    """
    seed = string.ascii_letters + string.digits
    result = ''
    for i in range(5):
        result += random.choice(seed)
    return prefix + result


class LineView(TemplateView):
    """ views for creating Line Chart """
    model = None
    name = "data"
    template_name = 'chartapp/lineplate.html'
    form = None

    # for color configuration
    colors = {}

    def prepare_fields(self):
        fields = self.model.objects.order_by('xfield')
        return fields

    def prepare_colors(self):
        """ prepare colors configuration for chart """
        colors = self.colors
        # check whether user has defined colors, if not generate random colors
        if not colors :
            random_colors = [ random.randrange(0, 255) for i in range(3)]
            colors = {
                'fillColor' : "rgba({},{},{},0.2)".format(*random_colors),
                'strokeColor': "rgba({},{},{},1)".format(*random_colors),
                'pointColor': "rgba({},{},{},1)".format(*random_colors),
                'pointStrokeColor': "#fff",
                'pointHighlightFill': "#fff",
                'pointHighlightStroke': "rgba({},{},{},1)".format(*random_colors),
            }
        return colors


    def get_context_data(self, **kwargs):
        context = kwargs
        context['line_data'] = {'name':self.name,
                               'fields':self.prepare_fields(),
                               'colors':self.prepare_colors(),
                               'id':random_string('line')}

        try :
            kwargs['POST_exists']
            context['form'] = self.form(request.POST)
        except KeyError:
            context['form'] = self.form()
        return context

    def get(self, request, *args, **kwargs):
        # check model is defined or not
        if not self.model:
            raise ModelMissing()
        return TemplateView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form .is_valid():
            form.save()
        else :
            kwargs['POSTS_exists'] = True
        return TemplateView.get(self, request, *args, **kwargs)


class DonutView(TemplateView):
    """ this views for showing pie chart """
    name = "Doughnut Data"
    model = None
    form = None
    template_name = 'chartapp/donutplate.html'

    def get_context_data(self, **kwargs):
        context = kwargs
        context['donut_data'] = {'fields':self.model.objects.all(),
                                  'id':random_string('donut')}

        print self.request.POST
        try :
            kwargs['POST_exists']
            context['form'] = self.form(self.request.POST)
        except KeyError:
            context['form'] = self.form()
        return context

    def get(self, request, *args, **kwargs):
        # make sure model is defined
        if not self.model:
            raise ModelMissing()
        return TemplateView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            if not data.color :
                # generate random colors if user doesn't input any colors
                random_colors = [ random.randrange(0, 255) for i in range(3)]
                data.color = "rgba({},{},{},1)".format(*random_colors)
            data.save()

        kwargs['POST_exists'] = True
        return TemplateView.get(self, request, *args, **kwargs)
