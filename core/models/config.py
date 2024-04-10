"""
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-04-08 17:45:06
LastEditTime: 2024-04-10 13:57:51
LastEditors: Night-stars-1 nujj1042633805@gmail.com
"""

# TODO: 将配置文件的数据模型方块化

import json
from pathlib import Path
from typing import Dict, List

from loguru import logger
from pydantic import BaseModel, Field

ROOT_PATH = Path().resolve()
"""项目根目录路径"""
CONFIG_PATH = ROOT_PATH / "config.json"
"""自动程序配置文件路径"""


class RestAreaModel(BaseModel):
    """休息区模型"""

    class RunTimeModel(BaseModel):
        runtime: float = 0.0
        """运行时间"""

    huashi: RunTimeModel = RunTimeModel()
    """桦石"""


class RSBModel(BaseModel):
    """铁安局模型"""

    city: str = "7号自由港"
    """刷取城市"""
    levelSerialPos: List[int] = [635, 662]
    """刷取关卡序号位置"""
    name: str = "所有"
    """刷取关卡名称 所有为全部刷取"""
    num: int = 1
    """刷取次数"""


class UserModel(BaseModel):
    """用户模型"""

    class CityLevelModel(BaseModel):
        """城市声望等级模型"""

        七号自由港: int = Field(0, alias="7号自由港")
        修格里城: int = 0
        曼德矿场: int = 0
        澄明数据中心: int = 0
        荒原站: int = 0

    class CityDataModel(BaseModel):
        """城市数据模型"""

        buy_num: float = 0.0
        """购买数量"""
        revenue: float = 0.0
        """收益"""

    class GoBackModel(BaseModel):
        """砍抬提价模型"""

        class RaisePriceModel(BaseModel):
            """往返砍抬模型"""

            percentage: float = 0.0
            """百分比"""
            profit: int = 0
            """利润"""

        raise_price: RaisePriceModel = RaisePriceModel()
        """抬价"""
        cut_price: RaisePriceModel = RaisePriceModel()
        """砍价"""

    class SkillLevelModel(BaseModel):
        """技能等级模型"""

        星花: int = 0
        卡洛琳: int = 0
        伊尔: int = 0
        菲妮娅: int = 0
        叶珏: int = 0
        黛丝莉: int = 0
        阿知波: int = 0
        塞西尔: int = 0
        瓦伦汀: int = 0
        魇: int = 0
        奈弥: int = 0
        甘雅: int = 0
        艾略特: int = 0
        朱利安: int = 0
        瑞秋: int = 0
        山岚: int = 0
        卡莲: int = 0
        静流: int = 0
        雷火: int = 0
        狮鬃: int = 0

    city_level: CityLevelModel = CityLevelModel()
    """城市等级"""
    city_data: Dict[str, CityDataModel] = {}
    """城市数据"""
    go: GoBackModel = GoBackModel()
    """出发配置"""
    back: GoBackModel = GoBackModel()
    """返回配置"""
    skill_level: SkillLevelModel = SkillLevelModel()
    """技能等级"""
    goods_addition: dict = {}
    """商品附加"""
    max_goods_num: int = 0
    """最大商品数量"""


class Config(BaseModel):
    """自动程序配置"""

    version: str = "1.0.0"
    """版本号"""
    rsb: RSBModel = RSBModel()
    """铁安局配置"""
    user: UserModel = UserModel()
    rest_area: RestAreaModel = RestAreaModel()
    """休息区配置"""

    def save_config(self):
        """保存配置"""
        try:
            str_data = self.model_dump_json(indent=4, by_alias=True)
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                f.write(str_data)
        except (AttributeError, TypeError, ValueError, PermissionError):
            logger.exception(
                f"保存配置文件失败，请检查是否有权限读取和写入 {CONFIG_PATH}"
            )
            raise
        else:
            logger.info(f"配置文件 {CONFIG_PATH} 已保存。")


if CONFIG_PATH.exists() and CONFIG_PATH.is_file():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    config = Config.model_validate(data)
else:
    config = Config()
    try:
        str_data = config.model_dump_json(indent=4)
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            f.write(str_data)
    except (AttributeError, TypeError, ValueError, PermissionError):
        logger.exception(f"创建配置文件失败，请检查是否有权限读取和写入 {CONFIG_PATH}")
        raise
    else:
        logger.info(f"配置文件 {CONFIG_PATH} 不存在，已创建默认插件配置文件。")
config.save_config()
