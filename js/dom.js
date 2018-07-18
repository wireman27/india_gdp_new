function changeListElement(number, text="", link="",attributeKey="style",attributeValue="") {
	links[0]["children"][number]["children"][0].innerText = text
	links[0]["children"][number]["children"][0].href = link
	links[0]["children"][number]["children"][0].setAttribute(attributeKey,attributeValue)
}

function compareToolUI() {
    document.getElementsByClassName("mapboxgl-control-container")[0].style.display = 'none';
    document.getElementById('map').style.display = 'block';
    changeListElement(0, "Choose any two states");
    for(i=2;i<4;i++) {
        changeListElement(i)
    }
    changeListElement(1,"Compare!","javascript:compareStates()","style","color:orange")
    changeListElement(2,"Back to Safety","javascript:backToHome()")
}

function goBackFromCompareUI() {
	var maps = document.getElementById('allmaps')
    var cmap1div = document.createElement("div")
    var cmap2div = document.createElement("div")

    cmap1div.classList.add('comparemaps')
    cmap1div.setAttribute("id","cmap1")
    cmap2div.classList.add('comparemaps')
    cmap2div.setAttribute("id","cmap2")

    maps.appendChild(cmap1div);
    maps.appendChild(cmap2div);
}

function compareStatesUI() {
    var comparedStates = "Comparing "+state1.properties.Name+" and "+state2.properties.Name

    changeListElement(0, comparedStates,"")
    changeListElement(1,"Go Back!","javascript:goBackFromCompare()")
    changeListElement(2)

    document.getElementById('map').style.display = 'none';
    document.getElementById('cmap1').style.display = 'block';
    document.getElementById('cmap2').style.display = 'block';
}

function backToHomeUI() {
	changeListElement(0, "Github", "https://github.com/wireman27/india_gdp_new", "target", "_blank")
	changeListElement(1, "QGIS Walkthrough", "https://wireman27.github.io/india_gdp_new/qgis_docs", "target", "_blank")
	changeListElement(1, "QGIS Walkthrough", "https://wireman27.github.io/india_gdp_new/qgis_docs", "style", "color:white")
	changeListElement(2, "Original Paper","http://www.ngdc.noaa.gov/eog/pubs/Ghosh_TOGEOGJ.pdf", "target", "_blank")
	changeListElement(3, "Compare States","javascript:compareTool()", "target", "_blank")
	changeListElement(3, "Compare States","javascript:compareTool()", "style", "color:orange")

	document.getElementsByClassName("mapboxgl-control-container")[0].style.display = 'block';

}