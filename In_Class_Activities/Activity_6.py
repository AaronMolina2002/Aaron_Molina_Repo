import Web_Scraping as wb

def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    main_tree = wb.get_web_tree("https://www.wvu.edu")
    print(main_tree.xpath)
    # Find any tag with the id wvu-main, then go down one level, and obtain whatever text there is.
    # Right-click on your browser and hit Inspect (Chrome is preferable)
    uni_name = main_tree.xpath('//*[@id="student-profile"]/div/div[1]/div[2]/h2/text()')
    #relationships = main_tree.xpath('//*[@id="oc_888_Relationships"]/div/div/div/div/div/text()')
    print(((uni_name)))
    #creating a variable to track the xpath
    uni_name1 = main_tree.xpath('//*[@id="resources"]/div/div[1]/h2/text()')
    #printing what the xpath finds
    print(((uni_name1)))
    # creating a variable to track the xpath
    uni_name2 = main_tree.xpath('//*[@id="resources"]/div/div[2]/p[2]/text()')
    # printing what the xpath finds
    print(((uni_name2)))
    # creating a variable to track the xpath
    uni_name3 = main_tree.xpath('//*[@id="wvu-main"]/div[4]/div/div[1]/h2/text()')
    # printing what the xpath finds
    print(((uni_name3)))
    # creating a variable to track the xpath
    uni_name4 = main_tree.xpath('//*[@id="resources"]/div/div[3]/div[2]/div/h3/text()')
    # printing what the xpath finds
    print(((uni_name4)))

if __name__ == "__main__":
    main()
