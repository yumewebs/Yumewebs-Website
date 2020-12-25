/*******CAMBIAR ATR. HEADER*******/
/**Hecho para solucionar problema del width del header */
$(window).on("scroll", function ()
{
    if ($(window).scrollTop() > $("#header").offset().top - 100)
    {
        $("#header").addClass("headerchange");
    } else
    {
        $("#header").removeClass("header");
    };
});

$(window).on("scroll", function ()
{
    if ($(window).scrollTop() > $("#header").offset().top + 150)
    {
        $("#header").addClass("header");
    } else
    {
        $("#header").removeClass("headerchange");
    };
});

/**Error Solucionado!! */