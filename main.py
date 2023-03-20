import pygame

# to match up the coordinates of the two objects and set a condition for the happening of collision.
import collisions

'''An event is an action that is performed by the user in order to get the desired result. 
For instance, if a user clicks a button then it is known as a click event. Now, all the events that are performed by 
the user are inserted into a queue known as an event queue. Since it is a queue, it follows the First In First Out rule 
i.e. element inserted first will come out first. In this case, when an event is created it is added to the back of the queue and 
when the event is processed then it comes out from the front. Every element in this queue is associated with an attribute which is nothing 
but an integer that represents what type of event it is.  Let us learn a few important attributes of the common event types.'''
import event

import gamestate
import graphics
import config

was_closed = False
while not was_closed:
    game = gamestate.GameState() 
    #game state is simply a way of referring to a set of values for all the variables in a game program
    button_pressed = graphics.draw_main_menu(game)

    #To start the game 

    if button_pressed == config.play_game_button: #To start the game 
        game.start_pool()

        #pygame module for interacting with events and queues
        events = event.events()
        while not (events["closed"] or game.is_game_over or events["quit_to_main_menu"]):
            events = event.events()
            collisions.resolve_all_collisions(game.balls, game.holes, game.table_sides)
            game.redraw_all()

            # to check the movement 
            if game.all_not_moving():
                game.check_pool_rules()
                game.cue.make_visible(game.current_player)
                while not (
                    (events["closed"] or events["quit_to_main_menu"]) or game.is_game_over) and game.all_not_moving():

                    '''It is often useful to refresh the image of the model or drawing, to remove extraneous vectors or highlighted surface borders. 
                       You can also use the Redraw All command to refresh the image if it should appear corrupted for any reason '''
                    game.redraw_all()
                    events = event.events()
                    if game.cue.is_clicked(events):
                        game.cue.cue_is_active(game, events)
                    elif game.can_move_white_ball and game.white_ball.is_clicked(events):
                        game.white_ball.is_active(game, game.is_behind_line_break())
        was_closed = events["closed"]

    # A condition has been passed to exit the game while press or click on exit button 
    if button_pressed == config.exit_button:
        was_closed = True
# use to close the game window 
pygame.quit()
