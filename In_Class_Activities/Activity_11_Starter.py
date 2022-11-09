"""
Activity #11 starter file
Insert bug id and bug packages to a DB
"""
import psycopg2
import Web_Scraping as wb

def main():
    """
    Main screen for the web scrapping file
    :return:
    """

    link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist" \
           "=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED" \
           "&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field" \
           ".importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance" \
           "%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type" \
           "%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA" \
           "&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field" \
           ".structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field" \
           ".status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field" \
           ".affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field" \
           ".has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field" \
           ".has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby" \
           "=-importance&memo=75&start=0 "

    main_tree = wb.get_web_tree(link)

    bug_list = main_tree.xpath('//*[@class="bugnumber"]//text()')
    # Get rid of # in each bug id, and return the clean list
    bug_list = [ele.replace('#', '') for ele in bug_list]
    print(str(len(bug_list)))
    print(bug_list)

    bug_package = main_tree.xpath('//*[@class="buginfo-extra"]/span/text()')
    # cleanup package names and only include elements which are not empty.
    # print(bug_package)
    bug_package = [ele for ele in ([ele.strip() for ele in bug_package]) if ele != '']
    print(bug_package)
    print(str(len(bug_package)))
    # Write your code here
    # 1. Create one DB table named [YourName]_Ubuntu, with two fields as varchar bug_id and bug_package
    my_db = MyDB()
    sqlCommand = 'CREATE TABLE IF NOT EXISTS Aaron_Ubuntu (bug_id  VARCHAR, bug_package  VARCHAR);'
    my_db.query(sqlCommand, '')
    # 2. Iterate through bug id's and bug packages and insert bug_id and package name to the table
    counter = 0
    while counter < len(bug_list):
        print(bug_list[counter])
        print(bug_package[counter])

        my_db = MyDB()
        sqlCommand = 'INSERT INTO Aaron_Ubuntu VALUES(%s, %s);'
        my_db.query(sqlCommand, (bug_list[counter], bug_package[counter],))

        counter = counter + 1

    # 3. Test whether table has been created and has data using SQL: SELECT * FROM [Table_Name].
    my_db = MyDB()
    sqlCommand = 'SELECT * FROM Aaron_Ubuntu;'
    d = my_db.query(sqlCommand, '')
    print(d)

    # 4. Drop the table from the DB.
    my_db = MyDB()
    sqlCommand = 'DROP TABLE Aaron_Ubuntu;'
    my_db.query(sqlCommand, '')

    # Connects you to your DB
    # my_db = MyDB()
    # This is how you write SQL statement to your DB
    # my_db.query(sqlCommand, '')

    # If you need to add data to a table, use this where each %s is a data element.
    # my_db = MyDB()
    # sqlCommand = f'INSERT INTO Aaron_Ubuntu VALUES({bug_list}, {bug_package});' #Assuming we have a table with one column only
    # my_db.query(sqlCommand, '')

    # Execute teh query, notice the extra , after the data
    #my_db.query(sqlCommand, ("CC",))

class MyDB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = psycopg2.connect(host='localhost', user='cyberUser', password='c-4-9-3-A',
                                               dbname='cybrDB')
        self._db_connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        first_return = self._db_cur.execute(query, params)
        try:
            return_me = self._db_cur.fetchall()
        except Exception:
            return_me = first_return
        return return_me

    def __del__(self):
        if self._db_connection is not None:
            self._db_connection.close()



if __name__ == "__main__":
    main()

