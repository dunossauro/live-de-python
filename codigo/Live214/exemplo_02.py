from rocketry import Rocketry

app = Rocketry()


@app.task('every 1s', execution='async')
async def todo_segundo_a():
    print('A')


@app.task('every 1s', execution='process')
async def todo_segundo_b():
    print('B')


app.run()
