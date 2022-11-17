import requests

from lxml import html

def get_web_tree(link):
    """
    This method gets a web page from the specified url, and returns a tree of all elements in the page
    :param link: The webpage to access and process
    :return: The tree element created from the page
    """
    # Welcome message
    print('Obtaining the page: ', str(link))
    # get the page
    page = requests.get(link)
    # get the elements from the page
    page_tree = html.fromstring(page.content)
    # return the tree of the web page
    return page_tree

# create a link for the first page of the website
initial_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start=0"
# Created a variable for the total number of bugs on the website
Bugs = 405409
# created a variable for the number of pages on the website and adding one to the total amount
Pages = (int(Bugs/75)) + 1
# created a page counter variable to add to the number of pages
Page_counter = 0
# created another count variable
Start_counter = 0
# created a variable to have a value of a string
newStart = ""
# created a while loop for the page counter to be less than the pages
while Page_counter < Pages:
    # set Start_counter to be equal to Page_counter and multiplying that value by 75
    Start_counter = Page_counter * 75
    # set newStart to equal to the added Start_counter
    newStart = Start_counter
    # set the initial link to have the newStart variable to be added to both &start= and &memo=
    initial_link = f"https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field" \
                   f".status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status" \
                   f"%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field" \
                   f".importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field" \
                   f".importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field" \
                   f".information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field" \
                   f".information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option" \
                   f"=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field" \
                   f".structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY" \
                   f"&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field" \
                   f".omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field" \
                   f".has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on" \
                   f"&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field" \
                   f".has_no_blueprints=on&search=Search&orderby=-importance&memo={newStart}&start={newStart} "
    # printed out what page the code is on and how many total pages there are
    print(f"This is page #{Page_counter} of {Pages}")
    # printed out the updated link
    print(initial_link)
    # added to the page counter variable by one
    Page_counter += 1

