def field(items, *args):
    assert len(args) > 0

    result = []

    if len(args) == 1:
        result = [item[args[0]] for item in items if args[0] in item.keys()]
    else:
        filtered_items = [item for item in items if any(arg in item.keys() for arg in args)]
        result = [{arg:item[arg] for arg in item.keys() if arg in args} for item in filtered_items]
                
    return result

if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    field(goods, 'title')
    field(goods, 'title', 'price')
