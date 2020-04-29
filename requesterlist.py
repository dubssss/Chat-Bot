import psycopg2

def getdata():
    con=psycopg2.connect(
            host="",
            database="test",
            user="postgres",
            password="")

    cur=con.cursor()
    cur.execute("select username,password from requester")
    rows=cur.fetchall()
    req_dict={}
    for i in rows:
        req_dict[i[0]]=i[1]

    cur.close()
    con.close()  
    return(req_dict)

if __name__=="__main__":
    getdata()


