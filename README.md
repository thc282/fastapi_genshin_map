<p align="center">
  <a href="https://github.com/KimigaiiWuyi/fastapi_genshin_map/"><img src="https://s2.loli.net/2022/01/31/kwCIl3cF1Z2GxnR.png" width="256" height="256" alt="Fastapi_Genshin_Map"></a>
</p>
<h1 align = "center">Fastapi_Genshin_Map<br>(from: KimigaiiWuyi)</h1>
<h4 align = "center">✨一个基于<a href="https://github.com/MingxuanGame/GenshinMap" target="_blank">GenshinMap</a>的地图API✨</h4>

## 安装

> *首次启动会等待一段时间, 属于正常现象*
1. `git clone`本项目到喜欢的位置  
或
2. 下載zip, 並解壓
---
## ❗❗注意事項
由於獲取所有地圖的時間長, 請耐心等候
直至出現以下INFO才算完結
```
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```

### 存放位置(資料夾)
`fastapi_genshin_map\map_data`

---
## 使用 (每次改完)
1. `cd` 至 `fastapi_genshin_map`
2. `python main.py`
   
<details>
  <summary><h3>如何獲取資源點地圖(全/選擇)</h3></summary>
  
由於暫時還沒有處理好輸入

以下給懂改coding的人
```py
# get_map_image.py
'line 60 --' # 指定地圖id或留空拿全部地圖
'line 61 --'  desired_map_ids = {35}
```
#### [預設]留空 — 獲取所有地圖 (提瓦特, 淵下宮, 層岩下層, 舊日之海, 希穆蘭卡)
例子:  
拿全部 — `desired_map_ids = {}`

=====================================================================================

#### 填ID — 獲取對應地圖 
| ID | 地圖 |
| - | - |
| 2 | 提瓦特 |
| 7 | 淵下宫 |
| 9 | 層岩巨淵·地下礦區 |
| 34 | 舊日之海 |
| 35 | 希穆蘭卡 |

例子:  
拿提瓦特, 淵下宮, 希穆蘭卡 — `desired_map_ids = {2, 7, 35}`  
拿提瓦特, 舊日之海 — `desired_map_ids = {2, 34}`
</details>

---
## 感谢
- [GenshinMap](https://github.com/MingxuanGame/GenshinMap) - 没有这个项目就不会有这个作品
- [KimigaiiWuyi](https://github.com/KimigaiiWuyi/fastapi_genshin_map/) - 感謝你的更改

---
## 许可证
该项目以`GPL-3.0 license`开源, 这意味着使用该项目的项目也将以`GPL-V3`开源


---
## 其他
+ 如果对本插件有功能建议&Bug报告，欢迎提Issue & Pr，每一条都会详细看过
+ 如果本插件对你有帮助，不要忘了点个Star~
+ 本项目仅供学习使用，请勿用于商业用途
+ [GPL-3.0 License](https://github.com/KimigaiiWuyi/GenshinUID/blob/main/LICENSE) ©

---
## 筆記(自用)
models.py — 加地圖ID  
download.py — 加world API  
get_map_image.py — 加path & path check  
