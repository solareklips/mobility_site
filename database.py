from sqlalchemy import create_engine, text
"""
FROM 27-08-2023
DB_HOST=aws.connect.psdb.cloud
DB_USERNAME=5tvmw86muyqspn2jdxxi
DB_PASSWORD=pscale_pw_udWRn08OuSpIPVTDPr7bUyQ9ybwEHJLinRHabWzmtPa
DB_NAME=mobility

FROM 26-08-2023
server = "aws.connect.psdb.cloud"
pw = "pscale_pw_TYQtOwUJPLPMY0iV9sqqZjEf3ZwwnyWbfMXT3jK3ULj"
user = "b607qgzbnaiunae54uuw"
"""

connection_db_string = "mysql+pymysql://5tvmw86muyqspn2jdxxi:pscale_pw_udWRn08OuSpIPVTDPr7bUyQ9ybwEHJLinRHabWzmtPa@aws.connect.psdb.cloud/mobility?charset=utf8mb4"


engine = create_engine(
  connection_db_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

""" DISSE FUNKTIONER VIRKER TIL AT KALDE ITEMS


  


# Accessing columns from the tuple
exercise_id = first_result[0]
exercise_name = first_result[1]
two_side = first_result[2]

print("Full DB: ", result_all)
print("Exercise ID:", exercise_id)
print("Exercise Name:", exercise_name)
print("Two Side:", two_side)

SLUT HER """