from flask import Blueprint, request, render_template, redirect, url_for
from exts import db
import re


class BaseModule(Blueprint):
    def __init__(self, name, import_name, url_prefix):
        super().__init__(name, import_name, url_prefix=url_prefix)


    # 展示图表 | 搜索数据
    def search_items(self, model, search_column, form_name, template_name):
        if request.method == "GET":
            items = model.query.all()
            return render_template(template_name, items=items)
        else:
            keyword = request.form.get(form_name)

            if keyword == "":
                return render_template(template_name, keyword=keyword)
            else:
                # 验证输入长度
                if len(keyword) > 50:
                    return render_template(template_name, error="输入过长")

                # 验证输入格式
                if not re.match(r'^[a-zA-Z\d\s\u4e00-\u9fa5]*$', keyword):
                    return render_template(template_name, error="无效的输入格式")

                # 去除首尾空白字符，以防止注入攻击
                keyword = keyword.strip()

                if not keyword:
                    return render_template(template_name, keyword=keyword)
                else:
                    items = model.query.filter(search_column.like("%" + keyword + "%")).all()
                    return render_template(template_name, items=items, keyword=keyword)


    # 增加数据
    def add_item(self, model, template_name):
        if request.method == "GET":
            return render_template(template_name)
        else:
            form_data = request.form.to_dict()

            # 编号不能为空
            if not form_data["number"]:
                return render_template(template_name, error="请输入编号")

            for key, value in form_data.items():
                # 去除首尾空白空格
                cleaned_value = value.strip()
                # 验证输入长度
                if len(cleaned_value) > 50:
                    return render_template(template_name, error="输入过长")
                # 验证输入格式
                if not re.match(r'^[a-zA-Z\d\s\u4e00-\u9fa5]*$', cleaned_value):
                    return render_template(template_name, error="无效的输入格式")
                form_data[key] = cleaned_value

            item = model(**form_data)

            db.session.add(item)
            db.session.commit()
            
            return redirect(url_for(f"{model.__tablename__}.{model.__tablename__}"))


    # 删除数据
    def delete_item(self, model, target):
        if request.method == "POST":
            if request.form.get("confirmed") == "true":
                item = model.query.filter(model.number == target).first()
                db.session.delete(item)
                db.session.commit()

        return redirect(url_for(f"{model.__tablename__}.{model.__tablename__}"))


    # 修正数据
    def correct_item(self, model, template_name, target):
        if request.method == "GET":
            return render_template(template_name)
        else:
            item = model.query.filter(model.number == target).first()

            for key, value in request.form.items():
                # 去除首尾空白空格
                cleaned_value = value.strip()
                # 验证输入长度
                if len(cleaned_value) > 50:
                    return render_template(template_name, error="输入过长")
                # 验证输入格式
                if not re.match(r'^[a-zA-Z\d\s\u4e00-\u9fa5]*$', cleaned_value):
                    return render_template(template_name, error="无效的输入格式")
                setattr(item, key, cleaned_value)

            db.session.commit()
            
            return redirect(url_for(f"{model.__tablename__}.{model.__tablename__}"))
