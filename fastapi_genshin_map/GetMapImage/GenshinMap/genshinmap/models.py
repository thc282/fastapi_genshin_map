from __future__ import annotations

from enum import IntEnum
from typing import List, Tuple, Optional, NamedTuple

from pydantic import HttpUrl, BaseModel, validator
import json


class MapID(IntEnum):
    """地圖 ID"""

    teyvat = 2
    """提瓦特"""
    enkanomiya = 7
    """淵下宫"""
    chasm = 9
    """層岩巨淵·地下礦區"""
    # golden_apple_archipelago = 10
    """金蘋果群島"""
    sea_of_bygone_eras = 34
    """舊日之海"""
    Simulanka = 35
    """希穆蘭卡"""


class Label(BaseModel):
    id: int
    name: str
    icon: HttpUrl
    parent_id: int
    depth: int
    node_type: int
    jump_type: int
    jump_target_id: int
    display_priority: int
    children: list
    activity_page_label: int
    area_page_label: List[int]
    is_all_area: bool


class Tree(BaseModel):
    id: int
    name: str
    icon: str
    parent_id: int
    depth: int
    node_type: int
    jump_type: int
    jump_target_id: int
    display_priority: int
    children: List[Label]
    activity_page_label: int
    area_page_label: List
    is_all_area: bool


class Point(BaseModel):
    id: int
    label_id: int
    x_pos: float
    y_pos: float
    author_name: str
    ctime: str
    display_state: int
    area_id: int
    ext_attrs: str
    z_level: int
    icon_sign: int


class Slice(BaseModel):
    url: HttpUrl


class Maps(BaseModel):
    slices: List[HttpUrl]
    origin: List[int]
    total_size: List[int]
    padding: List[int]

    @validator("slices", pre=True)
    def slices_to_list(cls, v):
        urls: List[str] = []
        for i in v:
            urls.extend(j["url"] for j in i)
        return urls


class DetailV2(BaseModel):
    total_size: Tuple[int, int]
    padding: Tuple[int, int]
    origin: Tuple[int, int]
    map_version: str
    min_zoom: int
    max_zoom: int
    original_map_size: Tuple[int, int]

    def calculate_size(self) -> Tuple[int, int]:
        return tuple((t - p) // 256 for t, p in zip(self.total_size, self.padding))


class MapInfo(BaseModel):
    id: int
    name: str
    parent_id: int
    depth: int
    detail: Optional[Maps]
    node_type: int
    children: list
    icon: Optional[HttpUrl]
    ch_ext: Optional[str]
    detail_v2: Optional[DetailV2]

    @validator("detail", pre=True)
    def parse_detail(cls, v):
        if isinstance(v, str):
            if v == "":
                return None
            try:
                return Maps.parse_raw(v)
            except json.JSONDecodeError:
                return v
        return v

    @validator("detail_v2", pre=True)
    def parse_detail_v2(cls, v):
        if isinstance(v, str):
            if v == "":
                return None
            try:
                return DetailV2.parse_raw(v)
            except json.JSONDecodeError:
                return v
        return v


class XYPoint(NamedTuple):
    x: float
    y: float


class XYZSPoint(NamedTuple):
    x: float
    y: float
    z: int
    s: int


class Kind(BaseModel):
    id: int
    name: str
    icon_id: int
    icon_url: HttpUrl
    is_game: int


class SpotKinds(BaseModel):
    list: List[Kind]
    is_sync: bool
    already_share: bool


class Spot(BaseModel):
    id: int
    name: str
    content: str
    kind_id: int
    spot_icon: str
    x_pos: float
    y_pos: float
    nick_name: str
    avatar_url: HttpUrl
    status: int


class SubAnchor(BaseModel):
    id: int
    name: str
    l_x: int
    l_y: int
    r_x: int
    r_y: int
    app_sn: str
    parent_id: str
    map_id: str
    sort: int


class Anchor(BaseModel):
    id: int
    name: str
    l_x: int
    l_y: int
    r_x: int
    r_y: int
    app_sn: str
    parent_id: str
    map_id: str
    children: List[SubAnchor]
    sort: int

    def get_children_all_left_point(self) -> List[XYPoint]:
        """获取所有子锚点偏左的 `XYPoint` 坐标"""
        return [XYPoint(x=i.l_x, y=i.l_y) for i in self.children]

    def get_children_all_right_point(self) -> List[XYPoint]:
        """获取所有子锚点偏右的 `XYPoint` 坐标"""
        return [XYPoint(x=i.r_x, y=i.r_y) for i in self.children]


class PageLabel(BaseModel):
    id: int
    name: str
    type: int
    pc_icon_url: str
    mobile_icon_url: str
    sort: int
    pc_icon_url2: str
    map_id: int
    jump_url: str
    jump_type: str
    center: Optional[Tuple[float, float]]
    zoom: Optional[float]

    @validator("center", pre=True)
    def center_str_to_tuple(cls, v: str) -> Optional[Tuple[float, float]]:
        if v and (splitted := v.split(",")):
            return tuple(map(float, splitted))  # type: ignore

    @validator("zoom", pre=True)
    def zoom_str_to_float(cls, v: str):
        if v:
            return float(v)
