# Chart app #

This is simple chartapp wrapper for line chart and django chart

### Notice ###
The development are using linux it should work properly even if you are using other OS.
but I cannot Guarantee it will 100% works.

### Requirements ###
* python 2.7
* django 1.6
* jquery 1.11

### Installation ###

* run `pip install -r requirements` to install necessary requirements
* then run `python setup.py install` or copy paste `chartapp` folder to your project location

### Running the demo ###

assuming you have installed the requirements and make sure that chartapp symbolic link in the
demo section aim to chartapp location;

* run `manage.py syncdb` to create the database
* run `manage.py runserver`
* then go to your browser and access localhost:8000


### Combining to your project ###
you need to extends chartapp.views in your views like so :

    from chartapp.views import LineView, DonutView

    class SomeChart(LineView): # use LineView for Line Chart or DonutView for Donut Chart
        model = SomeModel  # your model
        form = SomeForm   # your form validation

and in the your main urls add the views

    urlpatterns = patterns('',
        ...
        url(r'^chart', SomeChart.as_view(), name="line_view"),
        ...
    )

then you can acces it in `localhost:8000/chart`, check demo section how to implement it.

### Credits ###
this project using [Chartjs](http://www.chartjs.org/) to create the chart
and [bootstrap](http://getbootstrap.com/) for the demo basic css
