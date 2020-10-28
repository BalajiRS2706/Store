from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This field cannot be blank"
        )

    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field cannot be blank"
        )

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'A name with that username already exists'}

        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
            return {'message': 'An error occurred inserting the user'}, 500
       

        return {"message": "User created Successfully"}, 201