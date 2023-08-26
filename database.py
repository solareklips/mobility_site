from sqlalchemy import create_engine, text
"""
server = "aws.connect.psdb.cloud"
pw = "pscale_pw_TYQtOwUJPLPMY0iV9sqqZjEf3ZwwnyWbfMXT3jK3ULj"
user = "b607qgzbnaiunae54uuw"
"""

connection_db_string = "mysql+pymysql://b607qgzbnaiunae54uuw:pscale_pw_TYQtOwUJPLPMY0iV9sqqZjEf3ZwwnyWbfMXT3jK3ULj@aws.connect.psdb.cloud/mobility?charset=utf8mb4"


engine = create_engine(
  connection_db_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM exercises"))
  print("result.all(): ",result.all())
  print("type(result): ",type(result))
  result_all = result.all()
  print("type(result_all): ",type(result_all))
  print("result_all: ",result_all)
"""
  print(f"result: {result}")
  print("type(result): ", type(result))
  result_all = result.all()
  print("type(result.all()): ", type(result_all))
  first_result = result_all[0]
  print("type(first_result): ", type(first_result))
  first_result_dict = dict(first_result[0])
  print("type(first_result_dict): ", type(first_result_dict))
  print(first_result_dict)
"""