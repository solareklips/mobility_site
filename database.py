from sqlalchemy import create_engine, text

connection_db_string = "mysql+pymysql://wzqa20h70d2gjrqf422t:pscale_pw_hQAnZz8zoJBBQyYU21ncpgutL2XE8rQSDyfcBKWXGlc@aws.connect.psdb.cloud/mobility?charset=utf8mb4"

engine = create_engine(connection_db_string, connect_args={"ssl"{

}
}
)

with engine.connect() as connection:
  result = connection.execute(text("select * from exercises"))
  print(result.all())