import cloudinary
def consts(request):
    return dict(
        ICON_EFFECTS = dict(
            format="png",
            type="facebook",
            transformation=[
                dict(height=95, width=95, crop="thumb", gravity="face", effect="sepia", radius=20),
                dict(angle=10),
            ]
        ),
        THUMBNAIL = {
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 150, "width": 150,
        },
        #Modify the sample project’s gallery to display 2 additional thumbnails per image:
        #a. One with the Cloudinary logo as an overlay (watermark)
        THUMBNAIL_WATERMARK = {
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 150, "width": 150, "effect": "screen",
            "overlay": {'url': "https://res.cloudinary.com/demo/image/upload/logos/cloudinary_icon_blue.png"}, "crop": "fit",
        },
        #b. Second with the image saturation increased to 50%
        THUMBNAIL_SAT = {
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 150, "width": 150, "effect": "saturation:50",
        },
        CLOUDINARY_CLOUD_NAME = cloudinary.config().cloud_name
    )
