/*
This is 'capsule' a chartjs wrapper
using MIT see LICENSE for license details
Author : Firdan Machda
*/
var capsule = new function(){
    'use strict';

    function getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min)) + min;
    }

    this.wrapper = function (){
        var that=this,
            listOfData=[];

        function LineChartData(raw_data){
          // chart data structrure
            var that =this;

            this.labels=[];
            this.data=[];

            function parseData(raw_data){
              $.each(raw_data,function(i){
                // assign to zero if value does not exist
                  var value = raw_data[i].data ? raw_data[i].data:0;
                  that.labels.push(raw_data[i].label);
                  that.data.push(value);
              });
            }

            function insert(label,data){
              if (label && data ){
                for (var i = 0; i< that.labels.length; i++){
                  if (label < that.labels[i]){
                    that.labels.splice(index,0,label);
                    that.data.splice(index,0,data);
                    break;
                  }
                }
              } else {
                console.error('incomplete value ,label and data must be defined');
              }
            }

            function remove(label){
              if (label){
                index = that.labels.indexOf(label);
                that.labels.splice(index,0,1);
                that.data.splice(index,0,1);
              } else {
                console.error('incomplete value, label must be defined');
              }
            }

            parseData(raw_data);
        }

        function color(rgb){
          var r,g,b;
          if (rgb){
            r=rgb[0];
            g=rgb[1];
            b=rgb[2];
          }
          r=r?r:getRandomInt(10,225);
          g=g?g:getRandomInt(10,225);
          b=b?b:getRandomInt(10,225);
          return "rgba("+r+","+g+","+b;
        }

        function createLineDataset(data){
          var result = {'labels':[],'datasets':[]},
              rcolor;
          if (data.length){
              result.labels=data[0].data.labels;
              $.each(data,function(i){
                rcolor = color(data[i].color);
                result.datasets.push({
                    label: data[i].label_name,
                    fillColor: rcolor+",0.2)",
                    strokeColor: rcolor+",1)",
                    pointColor: rcolor+",1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: rcolor+",1)",
                    data: data[i].data.data,
                });
            });
          }
          return result;
        }

        function createDonutDataset(container){
          var result=[];
          $.each(container,function(i){
            result.push({
                'value':container[i].data,
                'label':container[i].label,
                'color':color(container[i].color)+",1)",
              });
            });
          return result;
        }

        function createChartjs(data,chartdata){
          // clear html
          $('#'+data.id).html('');

          var ctx = $('#'+data.id ).get(0).getContext('2d'),
              canvas =$('#'+data.id),
              option = assign(data.config),
              legendHolder = document.createElement('div'),
              helpers = Chart.helpers,
              dataset,chart;

          switch (data.type) {
            case 'line':
              var dataset = createLineDataset(chartdata);
              var chart = new Chart(ctx).Line(dataset,option);
              // generate legend
              legendHolder.innerHTML = chart.generateLegend();
              break;
            case 'polar':
              // polar has the same structure as donat chart
              dataset = createDonutDataset(chartdata);
              chart = new Chart(ctx).PolarArea(dataset,option)
            case 'donut':
              dataset = dataset ? dataset : createDonutDataset(chartdata);
              chart = chart ? chart : new Chart(ctx).Doughnut(dataset, option);

              // generate legend
              legendHolder.innerHTML = chart.generateLegend();
              helpers.each(legendHolder.firstChild.childNodes, function(legendNode,index){
                helpers.addEvent(legendNode, 'mouseover', function(){
                  var activeSegment = chart.segments[index];
                  activeSegment.save();
                  activeSegment.fillColor = activeSegment.highlightColor;
                  chart.showTooltip([activeSegment]);
                  activeSegment.restore();
                });
              });

              helpers.addEvent(legendHolder.firstChild,'mouseout',function(){
                chart.draw();
              });
              break;
          }
          canvas.parent().parent().children('.legend').html(legendHolder.firstChild);
        }

        function assign(config){
          var option;
          if (config){
              option = config;
          } else {
            // default option
           option={ showTooltips: true,
                    responsive:true,
                    pointHitDetectionRadius:3};
          }
          return option;
        }

        // function checkInside(value,arr){
        //   for (var i=0;i<arr.length;i++){
        //     if (value === arr[i]){
        //       return true;
        //     }
        //   }
        //   return false;
        // }

        function retrieve(data){
          // retrieve data from server
          $.get(data.source,function(tableData){
            var chartdata=[];
            switch(data.type){
              case 'line':
                // create Data
                $.each(tableData.data,function(i){
                  chartdata.push(
                    { 'label_name':tableData.data[i].label_name,
                      'data':new LineChartData(tableData.data[i].data),
                      'color':tableData.data[i].color
                    });
                });

                break;
              case 'polar':
              case 'donut':
                $.each(tableData,function(i){
                  chartdata.push(
                    { 'label':tableData[i].label,
                      'data':tableData[i].data,
                      'color':tableData[i].color,
                    });
                });
                break;
            }
            createChartjs(data,chartdata);
          });
        }

        function init(){
          var i;
          // retrieve from element
            $('canvas.chart').each(function(){
                listOfData.push({
                  'id': $(this).attr('id'),
                  'source': $(this).data('source'),
                  'config': $(this).data('config'),
                  'type': $(this).data('chartType'),
                });
            });

            for(var i=0; i < listOfData.length; i++){
              retrieve(listOfData[i]);
            }
        }

        init();
    };
};
