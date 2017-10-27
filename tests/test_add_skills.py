

def test_add_skills(app):
    app.session.login(username="ultras", password="KzkMK")
    app.group.add_skills()
