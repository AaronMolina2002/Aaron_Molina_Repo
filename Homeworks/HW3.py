from In_Class_Activities import Web_Scraping as wb
import re
"""
Homework #3 objective is to fill out and complete each of the following methods.    
    """

def Generate_Links_For_All_Bugs_Pages(link):
    """
        20 POINTS
       A method which creates an entire list of URLs of all bug pages of the initial link
       :param link: link to the initial launchpad vulnerabilities (page one) passed from main
       :return: list of URLs, each to a page of bugs
    """
    # Empty list, add all urls to this list
    main_tree = wb.get_web_tree(link)
    noOfBugs = main_tree.xpath('//*[@id="bugs-table-listing"]/div/table/tbody/tr/td/text()')[2]
    noOfBugs = [int(i) for i in noOfBugs.split() if i.isdigit()][0]

    noOfPages = (int(noOfBugs / 75)) + 1

    pageCounter = 0
    startCounter = 0
    newStart = ""
    bug_pages_list = []
    while pageCounter < noOfPages:
        startCounter = pageCounter * 75

        # Remove numbers at the end
        link = re.sub(r'\d+$', '', link)

        # combine page number with start string
        newStart = ('&start=' + str(startCounter))

        # combine page number with memo string
        memo = '&memo=' + str(startCounter)
        # print("newStart")
        # print(newStart)
        linkx = link.replace('&start=0', newStart)
        linkx = linkx.replace('&memo=75', memo)
        # print(linkx)
        bug_pages_list.append(linkx)
        pageCounter += 1

    # bug_pages_list = []

    # Each time you create a new link, store it in this variable
    current_link = f'{bug_pages_list}'

    # add the current link to the list
    bug_pages_list.append(current_link)

    return bug_pages_list


def GetBugIDs(page_link):
    """
    10 POINTS
        A method which iterates through the entire list of bug reports of any  given link
        :param link: link to launchpad bug report page passed from main
        :return: list of bug IDs of the page_link page
    """
    # Empty list, add all bug IDs to this list
    main_tree = wb.get_web_tree(page_link)

    bug_list = main_tree.xpath('//*[@class="bugnumber"]//text()')

    bug_list = [item.replace('#', '')for item in bug_list]

    return bug_list


def GetBugPackages(page_link):
    """
    20 POINTS
        A method which iterates through the entire list of bug reports of teh given link
        :param link: link to launchpad bug reports passed from main
        :return: list of bug packages of the page_link page
    """
    # Empty list, add all bug packages to this list
    main_tree = wb.get_web_tree(page_link)

    bug_package = main_tree.xpath('//*[@class="buginfo-extra"]//text()')

    bug_package = [x for x in bug_package if len(x) > 3]
    bug_package = [ele for ele in bug_package if ele.strip()]
    for i, s in enumerate(bug_package):
        bug_package[i] = s.strip()

    return bug_package


def GetTotalNumberOfBugs(page_link):
    """
    20 POINTS
        A method which gets extracts total number of bugs from the initial link of Ubuntu Vulnerabilities
        :param link: link to launchpad bug reports page
        :return: the total number of bugs from the first page
    """
    # Extract and clean total number of bugs
    main_tree = wb.get_web_tree(page_link)
    noOfBugs = main_tree.xpath('//*[@id="bugs-table-listing"]/div/table/tbody/tr/td/text()')[2]
    noOfBugs = [int(i) for i in noOfBugs.split() if i.isdigit()][0]

    return noOfBugs


def GetTotalNumberOfPages(page_link):
    """
    20 POINTS
            A method which calculates the total number of bug pages from the initial link of Ubuntu Vulnerabilities
            :param link: link to launchpad bug reports page
            :return: the total number of bug pages
        """

    # Extract and clean total number of bugs
    noOfPages = (int(GetTotalNumberOfBugs(page_link)/75)) + 1

    return noOfPages
