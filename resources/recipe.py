from flask_restful import Resource
from mysql_connector.errors import Error
from mysql_connection import get_connection
import 

### API를 만들기 위한 클래스 작성
### class(클래스)란? 변수와 함수로 구성된 묶음!
### 클래스는 상속이 가능하다.
### API를 만들기 위한 클래스는, flask_restful 라이브러리의 Rsource 클래스를 상속해서 만들어야한다.


class RecipelistResource(Resource):
    # restful api의 method에 해당하는 함수 작성
    def post(self) :
        # api 실행 코드를 여기에 작성
        
        # 클라이언트에서, body 부분에 작성한 json을 받아오는 코드
        data = request.get_json()

        print(data)

        return