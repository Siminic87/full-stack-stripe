# Django Blog Mini-Project

A simple blog app written using Django.

[![Build Status](https://travis-ci.org/Siminic87/django-blog.svg?branch=master)](https://travis-ci.org/Siminic87/django-blog)

https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/
https://stackoverflow.com/questions/38332868/restrict-each-user-to-only-vote-once-polls-django-python?noredirect=1&lq=1
https://stackoverflow.com/questions/1984047/django-filter-older-than-days



# Online Marketing - Issue Tracker
The “Online Marketing - Issue Tracker” is an online tool with which owners of small and medium sized businesses can post/upvote bugs and feature requests regarding the products and services that are offered on MarketingMan.ie.

## Demo
A live demo can be found at [Heroku: Cloud Application Platform](https://milestone-data-centric.herokuapp.com/)




## UX
The purpose of the Online Marketing Issue Tracker is to allow users to have a say in what products and bugs are tended to in terms of the products that offered on MarketingMan.ie. This is done via a voting system where bugs can be uptoved for free and feature requests at cost of 10$. 

The page is for any individual or company worldwide who has an interest in the products on MarketingMan.ie and would would like to influence the course of development.  

The Online Marketing Issue Tracker is the best way to influence the course of development at MarketingMan.ie because it gives a quick and comprehensive overview of bugs and featuer requests that have already been posted as well as allowing users to create topics of their own. Via the integrated voting system, users then have a quick and efficient way of having their say as to what bugs and features are tended to. 

- As a user type, I want to get a quick overview of bugs and feature requests that have already been posted by users of MarketingMan.ie. 
- As a user type, I want to be able to assess and vote on the urgency with which bugs and feature requests are developed.
- As a user type I want to be able to post, edit and delete bugs and feature requests that I would like to have tended to. 

### Mockups:
#### Desktop
![SEO User-Exchange Mockup - Desktop](/static/img/SEO-User-Exchange-Desktop.jpg)




#### Tablet / Mobile
![SEO User-Exchange Mockup - Tablet/Mobile](/static/img/SEO-User-Exchange-Tablet-Mobile.jpg)





## Features
The Online Marketing - Issue Tracker has various features that intend to allow users to get a quick overview of various bugs and feature requests that have been requested by other users. Users can then also post on vote on bugs and feature requests that they poersonnally would like to see tended to. 

### Existing Features
- List of database entries – All tips are summarized on a list individual cards. Information contained on the cards is tip title, tip description, tip category, number of up/downvotes, date of publishing and edit and delete functionality via links. Results are ordered by number of upvotes in descending order.
- 



All features fully responsive on mobile devices (incl. tablets and smartphones). 

### Features Left to Implement
- Full User Authentication including email and password verification
- Upvotes/Downvotes limited to just 1 per user
- Date selection for new tips auto set to current date. No past or future dates possible.

## Technologies Used
- HTML
    - The project uses HTML code to allow structuring and display of the information presented on MarketingMan.ie.
- [Python](https://www.python.org/) & [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - The logic for rendering the various app routes is written in Python coding language. In order to streamline this process, the Flask is a micro web framework written in Python was used.
- CSS
    - The project uses CSS code to visually design and animate the page's structure as defined by the HTML.
- [Bootstrap](https://getbootstrap.com/docs/3.3/)
    - The project uses the Bootstrap framework (v. 3.3.7) to save time in development by relying on standardized HTML and CSS elements that can be found in the library.
- [Materialize](http://archives.materializecss.com/0.100.2/)
    - The project uses the Materialize framework (v. 0.100.2) to save time in development by relying on standardized HTML and CSS elements that can be found in the library.
- [jQuery](https://blog.jquery.com/2017/03/20/jquery-3-2-1-now-available/) & [Bootstrap javascript](https://getbootstrap.com/docs/3.3/getting-started/)
    - The project uses jQuery (v. 3.2.1) and Boostrap javascript (v. 3.2.1) for animation and inclusion of portfolio carousel element.
- [D3](https://d3js.org/) & [DC](https://dc-js.github.io/dc.js/)
    - The project uses the D3 and DC javascript libraries for the purpose of summarising the databse entries on the portal.
- [Crossfilter](https://github.com/crossfilter/crossfilter)
    - The JavaScript library "Crossfilter" is used for grouping of data do that different charts can be compared based on results for selected data entries.
- [mLab Database](https://mlab.com/)
    - The project uses an mLab databse-as-a-service for storing the projects data and allowing manipulation of it. 

## Testing
1.  Quick overview of all posted Online Marketing tips / summary statistics
    1. Go to SEO User Exchange homepage
    2. Verify that summary statistics “total” and “new” display above tip card results and that “total” displays the total number of all results and “new” displays the number of results that were posted on the day of viewing the page.
    3. Verify that tips are ordered in descending order according to number of upvotes and that only 5 results are shown per page and that the remaining results can be accessed via the pagination links.
    4. Try to click on category links above results and verify that depending on selected category, only results for this category are displayed and that the summary statistics above the results change accordingly.
    5. Try to click on “summary” link in top navigation and verify that all 3 graphs (“Tips / Category”, “Upvotes / Tip” and “Tips / Date”) reflect current results and change dynamically when database is edited.

Manual testing revealed that the “tips overview” and “summary pages” were integrated and visualised seamlessly. The pages are accessible on all devices and all major browsers and look virtually the same on different browsers.

2.	Assessing and voting on usefulness of tips
    1. Go to SEO User Exchange homepage
    2. Try scrolling down results and verify that individual tip cards show number of received upvotes (See “Up:”).
    3. OR try to click on “Login” in main navigation and verify that individual tip cards now have an up- and downvote button.
    4. Try to click on either the up- or downvote button and verify that total number of upvotes of the chosen tip goes up or down accordingly.
    5. OR try to click on “login” in main navigation, click on the “Read More” button on an individual tip card (either on filtered or non-filtered results page) and verify that the individual tip card now has an up- and downvote button.
    6. Try to click on either the up- or downvote button and verify that total number of upvotes of the chosen tip goes up or down accordingly.

Manual testing revealed that assessing and voting on tips was integrated and visualised seamlessly. The functionality is accessible on all devices and all major browsers and looks virtually the same on different browsers. 

3.	Posting, editing and deleting tips (incl. tip categories)
    1. Go to SEO User Exchange homepage
    2. Try to click on “login” in top navigation, click “Add Tip!” button on the right of results OR ”New Tip” link in main navigation and verify that form for posting new tip loads correctly and includes fields for “category”, “name, “description” and publishing date.
    3. Try to choose tip category, enter tip name, tip description, select date of publishing, click “ADD TIP” below form and verify that user is redirected to unfiltered results page and that the new tip is included in results.
    4. OR try to click on “login” in main navigation, click on the “Read More” button on an individual tip card (either on filtered or non-filtered results page), click “EDIT” button and verify that tip form fields get populated correctly with data from chosen tip.
    5. Try making changes to pre-populated fields and click “SAVE TIP” and verify that user is redirected to unfiltered results page and that the edited tip is included in results.
    6. OR try to click on “login” in main navigation, click on the “Read More” button on an individual tip card (either on filtered or non-filtered results page), click “DEL” button and verify that browser throws pop-up asking “Are you sure?”.
    7. Try clicking “OK” and verify that user is redirected to unfiltered results page and that the deleted tip was removed from results.
    8. OR try clicking on “Manage Categories” link in main navigation and verify that all current categories are listed incl. an “EDIT” and “DEL” button and “Add New Category” button below results.
    9. Try clicking EDIT” button and verify that category form field gets populated correctly with data from chosen category.
    10. Try making changes to pre-populated field and click “SAVE CATEGORY” and verify that user is redirected to unfiltered results page and that the edited tip is included in results.
    11. OR Try clicking “DEL” button and verify that browser throws pop-up asking “Are you sure?”.
    12. Try clicking “OK” and verify that user is redirected to categories page and that the deleted category was removed from results.

Manual testing revealed that adding, editing and deleting tips/categories was integrated and visualised seamlessly. The functionality is accessible on all devices and all major browsers and looks virtually the same on different Browsers.

Major bug noticed when category buttons would not filter results at all and only render main summary page. Bug fixed by passing category correctly to template. Abother bug has appeared on Google Chrome browsers where the datepicker calendar closes before a date can be chosen on form pages. Resolution outstanding.

## Deployment
This site is hosted using Heroku: Cloud Application Platform.

Heroku Config Vars were set to:

- IP: 0.0.0.0
- PORT: 5000

The live site updates automatically each time there is a new push to its [GitHub repository](https://github.com/Siminic87/milestone-data-centric-final). You can git clone the code to run it locally on your machine.

## Credits
### Filtering Categories
Advice for filtering of tips categories ering of data charts from various pages of [stackoverflow.com](https://stackoverflow.com/)
