"""
https://www.w3schools.com/xml/xpath_intro.asp

Full path - Search input field
/html/body/div[2]/div[1]/div[1]/div[1]/input

Relative path - Search input field
//body/div[2]/div[1]/div[1]/div[1]/input

Several relatives
//body/div//div[1]/div[1]/input


Attributes
//input[@id]
//input[@id="tnb-google-search-input"]


//a[@class="w3-left w3-btn"]

Using round braces as elements are not siblings:
(//a[@class="w3-left w3-btn"])[2]

Any node
(//*[@class="w3-left w3-btn"])[2]

Contains function
(//div[contains(@class, "nextprev")]/a[contains(@class, "w3-left")])[1]


### Axes
(//div[@class="w3-clear nextprev"])[1]/child::*
(//div[@class="w3-clear nextprev"])[1]/ancestor::*[3]//h1
//a[@title="How to"]/following-sibling::*[1]
//a[@title="How to"]/preceding-sibling::*


### Functions
//a[contains(text(), "JAVA")]
//a[contains(., "JAVA")]
//*[contains(@class, "nav-btn")]

//div[@id="menubtn_container"]/../*[last()]
//div[@id="menubtn_container"]/../*[last()-1]

//div[@id="menubtn_container"]/../a[position()<3]

//*[starts-with(text(), "XPath")]
"""