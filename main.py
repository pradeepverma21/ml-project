from src.Red_Wine import logger

logger.info("My name is Pradeep")
logger.info("working on ml project")

from box import ConfigBox

data = ConfigBox({"name": "example"})
print(data.name)  
