# mx_online   Django框架web小应用--在线教育平台 <br/>    

## Django应用设计: <br/>

1. 用户模块               users
+ 1.1 模型类创建          users models.py
+ 1.2 自定义UserProfiles覆盖默认user表
+ 1.3 EmailVerifyRecord - 邮箱验证码
+ 1.4 Banner - 轮播图

2. 课程模块             courses
+ 2.1 模型类创建        courses models.py
+ 2.2 Course - 课程基本信息
+ 2.3 Lesson - 章节信息
+ 2.4 Video - 视频
+ 2.5 CourseResource - 课程资源

3. 课程机构模块         organization
+ 3.1 模型类创建        organization models.py
+ 3.2 CourseOrg - 课程机构基本信息
+ 3.3 Teacher - 教师基本信息
+ 3.4 CityDict - 城市信息

4. 用户操作模块         operation
+ 4.1 模型类创建        operation models.py
+ 4.2 UserAsk - 用户咨询
+ 4.3 CourseComments - 用户评论
+ 4.4 UserFavorite - 用户收藏
+ 4.5 UserMessage - 用户消息
+ 4.6 UserCourse - 用户学习的课程

#### [来源于:](http://coding.imooc.com/class/78.html)
