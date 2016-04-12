function getStreamgraphSettings()
{
     var s = new Settings();
    s.show_settings = true;
    s.show_legend = false;
    
    // Add the PitchColorPicker function defined below.
    s.ColorPicker.values.push("Pitch");
    s.ColorPicker.current = "Pitch";
    return s;

}

function PitchColorPicker(layers)
{
    // Rainbow. This is way too much color, just done to show how.
    var colors = [-13631744, -6226176, -7424, -42496, -65536, -65536, -5832704, -10354507, -12386062, -16776961, -16743169, -16711720];
    var pitches = getStreamgraphLabels();
    var color_map = {};
    for (var i = 0; i < colors.length; i++)
        color_map[pitches[i]] = colors[i];
    
    for (var i = 0; i < layers.length; i++)
    {
        layers[i].rgb = color_map[layers[i].name];
    }
}

function getStreamgraphData()
{
    return matrix
}

function getStreamgraphLabels()
{

    return categories;
}