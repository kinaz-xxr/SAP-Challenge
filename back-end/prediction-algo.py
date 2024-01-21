from app import db, app 

# def predictionAlgo(baySetUp, request : AppointMentObject):

def query_table(table_name):
    with app.app_context():
        table_class = globals().get(table_name)
        print(table_class)
        if table_class:
            # Query the table
            results = table_class.query.all()

            # Process the results as needed
            print(f"Results for {table_name}:")
            for row in results:
                print(row.__dict__)
            print("\n")

query_table('BayTable1')
