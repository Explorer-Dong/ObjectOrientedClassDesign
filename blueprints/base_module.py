from flask import Blueprint, request, render_template, redirect, url_for
from exts import db


class BaseModule(Blueprint):
    def __init__(self, name, import_name, url_prefix):
        super().__init__(name, import_name, url_prefix=url_prefix)


    def search_items(self, model, search_column, form_name, template_name):
        if request.method == "GET":
            items = model.query.all()
            return render_template(template_name, items=items)
        else:
            keyword = request.form.get(form_name)

            if keyword == "":
                return render_template(template_name, keyword=keyword)
            else:
                # 模糊查询
                items = model.query.filter(search_column.like("%" + keyword + "%")).all()
                return render_template(template_name, items=items, keyword=keyword)


    def add_item(self, model, template_name):
        if request.method == "GET":
            return render_template(template_name)
        else:
            form_data = request.form.to_dict()
            item = model(**form_data)

            db.session.add(item)
            db.session.commit()
            return redirect(url_for(f"{model.__tablename__}.{model.__tablename__}"))


    def delete_item(self, model, target):
        if request.method == "POST":
            if request.form.get("confirmed") == "true":
                item = model.query.filter(model.number == target).first()
                db.session.delete(item)
                db.session.commit()
        return redirect(url_for(f"{model.__tablename__}.{model.__tablename__}"))


    def correct_item(self, model, template_name, target):
        if request.method == "GET":
            return render_template(template_name)
        else:
            item = model.query.filter(model.number == target).first()

            for key, value in request.form.items():
                setattr(item, key, value)

            db.session.commit()
            return redirect(url_for(f"{model.__tablename__}.{model.__tablename__}"))
