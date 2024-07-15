
def _get_network_template():
    result = """<html>
    <head>
        <meta charset="utf-8">
        {% if cdn_resources=="local" %}
            <script src="lib/bindings/utils.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/dist/vis-network.min.css" integrity="sha512-WgxfT5LWjfszlPHXRmBWHkV2eceiWTOBvrKCNbdgDYTHrT2AeLCGbF4sZlZw3UMN3WtL0tGUoIAKsu8mllg/XA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js" integrity="sha512-LnvoEWDFrqGHlHmDD2101OrLcbsfkrzoSpvtSQtxK3RMnRV0eOkhhBN2dXHKRrUU8p2DGRTk35n4O8nWSVe1mQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
            {% if select_menu or filter_menu %}
                <link href="lib/tom-select/tom-select.css" rel="stylesheet">
                <script src="lib/tom-select/tom-select.complete.min.js"></script>
            {%  endif %}
        {% elif cdn_resources=="in_line" %}
            <script>{%  include 'lib/bindings/utils.js' %}</script>
            <style>{%  include 'lib/vis-9.1.2/vis-network.css' %}</style>
            <script>{%  include 'lib/vis-9.1.2/vis-network.min.js' %}</script>
            {% if select_menu or filter_menu %}
                <style>{%  include 'lib/tom-select/tom-select.css' %}</style>
                <script>{%  include 'lib/tom-select/tom-select.complete.min.js' %}</script>
            {%  endif %}
        {% endif %}
<center>
<h1>{{heading}}</h1>
</center>

<!-- <link rel="stylesheet" href="../node_modules/vis/dist/vis.min.css" type="text/css" />
<script type="text/javascript" src="../node_modules/vis/dist/vis.js"> </script>-->
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
          crossorigin="anonymous"
        />
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
          crossorigin="anonymous"
        ></script>


        <center>
          <h1>{{heading}}</h1>
        </center>
        <style type="text/css">

             #mynetwork {
                 width: {{width}};
                 height: {{height}};
                 background-color: {{bgcolor}};
                 border: 1px solid lightgray;
                 position: relative;
                 float: left;
             }

             {% if nodes|length > 100 and physics_enabled %}
             #loadingBar {
                 position:absolute;
                 top:0px;
                 left:0px;
                 width: {{width}};
                 height: {{height}};
                 background-color:rgba(200,200,200,0.8);
                 -webkit-transition: all 0.5s ease;
                 -moz-transition: all 0.5s ease;
                 -ms-transition: all 0.5s ease;
                 -o-transition: all 0.5s ease;
                 transition: all 0.5s ease;
                 opacity:1;
             }

             #bar {
                 position:absolute;
                 top:0px;
                 left:0px;
                 width:20px;
                 height:20px;
                 margin:auto auto auto auto;
                 border-radius:11px;
                 border:2px solid rgba(30,30,30,0.05);
                 background: rgb(22, 133, 136); /* Old browsers */
                 box-shadow: 2px 0px 4px rgba(0,0,0,0.4);
             }

             #border {
                 position:absolute;
                 top:10px;
                 left:10px;
                 width:500px;
                 height:23px;
                 margin:auto auto auto auto;
                 box-shadow: 0px 0px 4px rgba(0,0,0,0.2);
                 border-radius:10px;
             }

             #text {
                 position:absolute;
                 top:8px;
                 left:530px;
                 width:30px;
                 height:50px;
                 margin:auto auto auto auto;
                 font-size:22px;
                 color: #000000;
             }

             div.outerBorder {
                 position:relative;
                 top:400px;
                 width:600px;
                 height:44px;
                 margin:auto auto auto auto;
                 border:8px solid rgba(0,0,0,0.1);
                 background: rgb(252,252,252); /* Old browsers */
                 background: -moz-linear-gradient(top,  rgba(252,252,252,1) 0%, rgba(237,237,237,1) 100%); /* FF3.6+ */
                 background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(252,252,252,1)), color-stop(100%,rgba(237,237,237,1))); /* Chrome,Safari4+ */
                 background: -webkit-linear-gradient(top,  rgba(252,252,252,1) 0%,rgba(237,237,237,1) 100%); /* Chrome10+,Safari5.1+ */
                 background: -o-linear-gradient(top,  rgba(252,252,252,1) 0%,rgba(237,237,237,1) 100%); /* Opera 11.10+ */
                 background: -ms-linear-gradient(top,  rgba(252,252,252,1) 0%,rgba(237,237,237,1) 100%); /* IE10+ */
                 background: linear-gradient(to bottom,  rgba(252,252,252,1) 0%,rgba(237,237,237,1) 100%); /* W3C */
                 filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fcfcfc', endColorstr='#ededed',GradientType=0 ); /* IE6-9 */
                 border-radius:72px;
                 box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
             }
             {% endif %}

             {% if conf %}
             #config {
                 float: left;
                 width: 400px;
                 height: 600px;
             }
             {% endif %}

             {% if tooltip_link %}
             /* position absolute is important and the container has to be relative or absolute as well. */
          div.popup {
                 position:absolute;
                 top:0px;
                 left:0px;
                 display:none;
                 background-color:#f5f4ed;
                 -moz-border-radius: 3px;
                 -webkit-border-radius: 3px;
                 border-radius: 3px;
                 border: 1px solid #808074;
                 box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
          }

          /* hide the original tooltip */
          .vis-tooltip {
            display:none;
          }
             {% endif %}
        </style>
    </head>


    <body>
        <h3>네트워크</h3>
        <div class="card" style="width: 100%">
            {% if select_menu %}
                <div id="select-menu" class="card-header">
                    <div class="row no-gutters">
                        <div class="col-10 pb-2">
                            <select
                            class="form-select"
                            aria-label="Default select example"
                            onchange="selectNode([value]);"
                            id="select-node"
                            placeholder="Select node..."
                            >
                                <option selected>Select a Node by ID</option>
                                {% for node in nodes %}
                                    <option value="{{ node.id }}">{{node.id}}</option>
                                {% endfor %}
                            </select>
                        </div>
                        <div class="col-2 pb-2">
                            <button type="button" class="btn btn-primary btn-block" onclick="neighbourhoodHighlight({nodes: []});">Reset Selection</button>
                        </div>
                    </div>
                </div>
            {% endif %}
            {% if filter_menu %}
              <div id="filter-menu" class="card-header">
                <div class="row no-gutters">
                  <div class="col-3 pb-2">
                    <select
                            class="form-select"
                            aria-label="Default select example"
                            onchange="updateFilter(value, 'item')"
                            id="select-item"
                        >
                        <option value="">Select a network item</option>
                        <option value="edge">edge</option>
                        <option value="node">node</option>
                    </select>
                  </div>
                  <div class="col-3 pb-2">
                    <select
                            class="form-select"
                            aria-label="Default select example"
                            onchange="updateFilter(value, 'property')"
                            id="select-property"
                        >
                        <option value="">Select a property...</option>
                    </select>
                  </div>
                  <div class="col-3 pb-2">
                    <select
                            class="form-select"
                            aria-label="Default select example"
                            id="select-value"
                        >
                        <option value="">Select value(s)...</option>
                    </select>
                  </div>
                  <div class="col-1 pb-2">
                    <button type="button" class="btn btn-primary btn-block" onclick="highlightFilter(filter);">Filter</button>
                  </div>
                  <div class="col-2 pb-2">
                    <button type="button" class="btn btn-primary btn-block" onclick="clearFilter(true)">Reset Selection</button>
                  </div>
                </div>
              </div>
            {% endif %}
            <div id="mynetwork" class="card-body"></div>
        </div>

        {% if nodes|length > 100 and physics_enabled %}
            <div id="loadingBar">
              <div class="outerBorder">
                <div id="text">0%</div>
                <div id="border">
                  <div id="bar"></div>
                </div>
              </div>
            </div>
        {% endif %}
        {% if conf %}
            <div id="config"></div>
        {% endif %}

        <script type="text/javascript">

              // initialize global variables.
              var edges;
              var nodes;
              var allNodes;
              var allEdges;
              var nodeColors;
              var originalNodes;
              var network;
              var container;
              var options, data;
              var filter = {
                  item : '',
                  property : '',
                  value : []
              };

              {% if select_menu %}
                  new TomSelect("#select-node",{
                      create: false,
                      sortField: {
                          field: "text",
                          direction: "asc"
                      }
                  });
              {%  endif %}

              {% if filter_menu %}
                  // explicitly using onItemAdd and this function as we need to save multiple values
                  let updateValueFilter = function() {
                      return function () {
                      filter['value'].push(arguments[0])
                      }
                  }

                  let valueControl = new TomSelect("#select-value",{
                      maxItems: null,
                      valueField: 'id',
                      labelField: 'title',
                      searchField: 'title',
                      create: false,
                      sortField: {
                          field: "text",
                          direction: "asc"
                      },
                      onItemAdd: updateValueFilter()
                  });

                  let addValues = function() {
                      return function () {
                          // clear the current value options and add the selected attribute values
                          // tom-select handles duplicates
                          let selectedProperty = arguments[0];
                          valueControl.clear();
                          valueControl.clearOptions();
                          filter['value'] = []
                          if (filter['item'] === 'node') {
                              for (let each in allNodes) {
                                  valueControl.addOption({
                                      id:allNodes[each][selectedProperty],
                                      title:allNodes[each][selectedProperty]
                                  })
                              }
                          }
                          else if (filter['item'] === 'edge') {
                              for (let each in allEdges) {
                                  valueControl.addOption({
                                      id:allEdges[each][selectedProperty],
                                      title:allEdges[each][selectedProperty]
                                  })
                              }
                          }
                      }
                  };

                  let propControl = new TomSelect("#select-property",{
                      valueField: 'id',
                      labelField: 'title',
                      searchField: 'title',
                      create: false,
                      sortField: {
                          field: "text",
                          direction: "asc"
                      },
                      onItemAdd: addValues()
                  });

                  let addProperties = function() {
                      return function () {
                          // loops through the selected network item and adds the attributes to dropdown
                          // tom-select handles duplicates
                          clearFilter(false)
                          if (arguments[0] === 'edge') {
                              for (let each in allEdges) {
                                  if (allEdges.hasOwnProperty(each)) {
                                      for (let eachProp in allEdges[each]) {
                                          if (allEdges[each].hasOwnProperty(eachProp)) {
                                              propControl.addOption({id: eachProp, title: eachProp})
                                          }
                                      }
                                  }
                              }
                          }
                          else if (arguments[0] === 'node') {
                              for (let each in allNodes) {
                                  if (allNodes.hasOwnProperty(each)) {
                                      for (let eachProp in allNodes[each]) {
                                          if (allNodes[each].hasOwnProperty(eachProp)
                                              && (eachProp !== 'hidden' && eachProp !== 'savedLabel'
                                                  && eachProp !== 'hiddenLabel')) {
                                              propControl.addOption({id: eachProp, title: eachProp})

                                          }
                                      }
                                  }
                              }
                          }
                      }
                  };

                  let itemControl = new TomSelect("#select-item",{
                      create: false,
                      sortField:{
                          field: "text",
                          direction: "asc"
                      },
                      onItemAdd: addProperties()
                  });

                  function clearFilter(reset) {
                      // utility function to clear all the selected filter options
                      // if reset is set to true, the existing filter will be removed
                      // else, only the dropdown options are cleared
                      propControl.clear();
                      propControl.clearOptions();
                      valueControl.clear();
                      valueControl.clearOptions();
                      filter = {
                          item : '',
                          property : '',
                          value : []
                      }
                      if (reset) {
                          itemControl.clear();
                          filterHighlight({nodes: []})
                      }
                  }

                  function updateFilter(value, key) {
                      // key could be 'item' or 'property' and value is as selected in dropdown
                      filter[key] = value
                  }

              {%  endif %}

              // This method is responsible for drawing the graph, returns the drawn network
              function drawGraph() {
                  var container = document.getElementById('mynetwork');

                  {% if use_DOT %}

                  var DOTstring = "{{dot_lang|safe}}";
                  var parsedData = vis.network.convertDot(DOTstring);

                  data = {
                    nodes: parsedData.nodes,
                    edges: parsedData.edges
                  }

                  var options = parsedData.options;
                  options.nodes = {
                      shape: "dot"
                  }

                  {% else %}

                  // parsing and collecting nodes and edges from the python
                  nodes = new vis.DataSet({{nodes|tojson}});
                  edges = new vis.DataSet({{edges|tojson}});

                  nodeColors = {};
                  allNodes = nodes.get({ returnType: "Object" });
                  for (nodeId in allNodes) {
                    nodeColors[nodeId] = allNodes[nodeId].color;
                  }
                  allEdges = edges.get({ returnType: "Object" });
                  // adding nodes and edges to the graph
                  data = {nodes: nodes, edges: edges};

                  var options = {{options|safe}};

                  {% endif %}


                  {% if conf %}
                  // if this network requires displaying the configure window,
                  // put it in its div
                  options.configure["container"] = document.getElementById("config");
                  {% endif %}

                  network = new vis.Network(container, data, options);

                  {% if neighborhood_highlight %}
                    network.on("click", neighbourhoodHighlight);
                  {% endif %}

                  {% if select_menu %}
                    network.on("selectNode", neighbourhoodHighlight);
                  {% endif %}

                  {% if tooltip_link %}
                  // make a custom popup
                      var popup = document.createElement("div");
                      popup.className = 'popup';
                      popupTimeout = null;
                      popup.addEventListener('mouseover', function () {
                          console.log(popup)
                          if (popupTimeout !== null) {
                              clearTimeout(popupTimeout);
                              popupTimeout = null;
                          }
                      });
                      popup.addEventListener('mouseout', function () {
                          if (popupTimeout === null) {
                              hidePopup();
                          }
                      });
                      container.appendChild(popup);


                      // use the popup event to show
                      network.on("showPopup", function (params) {
                          showPopup(params);
                      });

                      // use the hide event to hide it
                      network.on("hidePopup", function (params) {
                          hidePopup();
                      });

                      // hiding the popup through css
                      function hidePopup() {
                          popupTimeout = setTimeout(function () { popup.style.display = 'none'; }, 500);
                      }

                      // showing the popup
                      function showPopup(nodeId) {
                          // get the data from the vis.DataSet
                          var nodeData = nodes.get([nodeId]);
                          popup.innerHTML = nodeData[0].title;

                          // get the position of the node
                          var posCanvas = network.getPositions([nodeId])[nodeId];

                          // get the bounding box of the node
                          var boundingBox = network.getBoundingBox(nodeId);

                          //position tooltip:
                          posCanvas.x = posCanvas.x + 0.5 * (boundingBox.right - boundingBox.left);

                          // convert coordinates to the DOM space
                          var posDOM = network.canvasToDOM(posCanvas);

                          // Give it an offset
                          posDOM.x += 10;
                          posDOM.y -= 20;

                          // show and place the tooltip.
                          popup.style.display = 'block';
                          popup.style.top = posDOM.y + 'px';
                          popup.style.left = posDOM.x + 'px';
                      }
                  {% endif %}


                  {% if nodes|length > 100 and physics_enabled %}
                      network.on("stabilizationProgress", function(params) {
                          document.getElementById('loadingBar').removeAttribute("style");
                          var maxWidth = 496;
                          var minWidth = 20;
                          var widthFactor = params.iterations/params.total;
                          var width = Math.max(minWidth,maxWidth * widthFactor);
                          document.getElementById('bar').style.width = width + 'px';
                          document.getElementById('text').innerHTML = Math.round(widthFactor*100) + '%';
                      });
                      network.once("stabilizationIterationsDone", function() {
                          document.getElementById('text').innerHTML = '100%';
                          document.getElementById('bar').style.width = '496px';
                          document.getElementById('loadingBar').style.opacity = 0;
                          // really clean the dom element
                          setTimeout(function () {document.getElementById('loadingBar').style.display = 'none';}, 500);
                      });
                  {% endif %}

                  return network;

              }
              drawGraph();
        </script>
    </body>
</html>
"""
    return result
