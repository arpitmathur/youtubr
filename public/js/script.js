function getStreamgraphSettings()
{
    var s = new Settings();
    s.show_settings = true;
    s.show_legend = false;
    
    s.colors.background = 200;
    s.colors.neutral = 100;
    s.colors.highlight = 0;
    
    // Change the color source used for the LastFm color picker.
    s.colors.image = "./js/deps/layers";
    return s;
}

function getStreamgraphData()
{
    return matrix
}

function getStreamgraphLabels()
{

    return categories;
}