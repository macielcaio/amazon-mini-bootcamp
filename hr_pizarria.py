class Profiles:

    def italian(self):
        return {
            "name": "Italian",
            "description": "A profile for Italian cuisine, focusing on traditional dishes and ingredients.",
            "cuisine_type": "Italian",
            "dishes": [
                "Pasta Carbonara",
                "Margherita Pizza",
                "Tiramisu"
            ],
            "ingredients": [
                "Olive oil",
                "Garlic",
                "Parmesan cheese"
            ]
        }
    def romanian(self):
        return {
            "name": "Romanian",
            "description": "A profile for Romanian cuisine, highlighting hearty and rustic dishes.",
            "cuisine_type": "Romanian",
            "dishes": [
                "Sarmale (Cabbage Rolls)",
                "Mămăligă (Polenta)",
                "Ciorbă de burtă (Tripe Soup)"
            ],
            "ingredients": [
                "Cabbage",
                "Cornmeal",
                "Garlic"
            ]
        }
    def mexican(self):
        return {
            "name": "Mexican",
            "description": "A profile for Mexican cuisine, featuring vibrant and spicy flavors.",
            "cuisine_type": "Mexican",
            "dishes": [
                "Tacos al Pastor",
                "Guacamole",
                "Chiles Rellenos"
            ],
            "ingredients": [
                "Chili peppers",
                "Cilantro",
                "Lime"
            ]
        }
    def american(self):
        return {
            "name": "American",
            "description": "A profile for American cuisine, known for its diversity and regional specialties.",
            "cuisine_type": "American",
            "dishes": [
                "Cheeseburger",
                "BBQ Ribs",
                "Apple Pie"
            ],
            "ingredients": [
                "Ground beef",
                "Barbecue sauce",
                "Apples"
            ]
        }