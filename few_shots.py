few_shots = [
    {
        "Question": "How many t-shirts do we have left for Nike in XS size and white color?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
        "SQLResult": "Result of the SQL query",
        "Answer": "91"
    },
    {
        "Question": "How much is the total price of the inventory for all S-size t-shirts?",
        "SQLQuery": "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE size = 'S'",
        "SQLResult": "Result of the SQL query",
        "Answer": "22292"
    },
    {
        "Question": "If we have to sell all the Levi's T-shirts today with discounts applied, how much revenue will our store generate?",
        "SQLQuery": """
            SELECT SUM(a.total_amount * ((100 - COALESCE(d.pct_discount, 0)) / 100)) AS total_revenue
            FROM (
                SELECT t_shirt_id, SUM(price * stock_quantity) AS total_amount
                FROM t_shirts
                WHERE brand = 'Levi'
                GROUP BY t_shirt_id
            ) a
            LEFT JOIN discounts d ON a.t_shirt_id = d.t_shirt_id;
        """,
        "SQLResult": "Result of the SQL query",
        "Answer": "16725.4"
    },
    {
        "Question": "If we have to sell all the Levi's T-shirts today, how much revenue our store will generate without any discount?",
        "SQLQuery": "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
        "SQLResult": "Result of the SQL query",
        "Answer": "17462"
    },
    {
        "Question": "How many white color Levi's shirts do I have?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
        "SQLResult": "Result of the SQL query",
        "Answer": "290"
    },
    {
        "Question": "How much sales amount will be generated if we sell all large size Nike t-shirts today after discounts?",
        "SQLQuery": """
            SELECT SUM(a.total_amount * ((100 - COALESCE(d.pct_discount, 0)) / 100)) AS total_revenue
            FROM (
                SELECT t_shirt_id, SUM(price * stock_quantity) AS total_amount
                FROM t_shirts
                WHERE brand = 'Nike' AND size = 'L'
                GROUP BY t_shirt_id
            ) a
            LEFT JOIN discounts d ON a.t_shirt_id = d.t_shirt_id;
        """,
        "SQLResult": "Result of the SQL query",
        "Answer": "2144.8"
    },
    {
        "Question": "How many Levi's t-shirts do we have?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
        "SQLResult": "Result of the SQL query",
        "Answer": "174"
    }
]
