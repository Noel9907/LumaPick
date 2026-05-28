from fastapi import APIRouter
from services.album import album,likeImage,GetImage
router = APIRouter()

router.add_api_route("/album",album,methods=['POST'])
router.add_api_route("/image",GetImage,methods=['GET'])
router.add_api_route("/like",likeImage,methods=['POST'])