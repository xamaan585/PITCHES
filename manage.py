from app import create_app,db
from flask_script import Manager,Server

# Creating app instance
app = create_app('develoment')

manager = Manager(app)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User=User,Pitch=Pitch,Upvote=Upvote,Downvote=Downvote,Comment=Comment)
if __name__ == '__main__':
    manager.run()