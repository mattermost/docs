# Mentioning Teammates
_____

## @Mentions
Use @mentions to get the attention of specific team members.

#### @Username
You can mention a teammate by using the `@` symbol plus their username to send them a mention notification. Type `@` and you will see a list of team members who can be mentioned. Completely type a username or use the **Up** and **Down** arrow keys and then **ENTER** to select them to be mentioned.

The following example sends a special mention notification to **alice** that alerts her of the channel and message where she has been mentioned. If **alice** is away from Mattermost and has [email notifications](http://docs.mattermost.com/help/getting-started/configuring-notifications.html#email-notifications) turned on, then she will receive an email alert of her mention along with the message text.

```
@alice how did your interview go with the new candidate?
```

If the user you mentioned does not belong to the channel, a System Message will be posted to let you know. This is a temporary message only seen by the person who triggered it. To add the mentioned user to the channel, go to the dropdown menu beside the channel name and select **Add Members**. 

#### @Channel
You can mention an entire channel by typing `@channel`. All members of the channel will receive a mention notification that behaves the same way as if the members had been mentioned personally.

```
@channel great work on interviews this week. I think we found some excellent potential candidates!
```

## Words That Trigger Mentions
In addition to being notified by @username and @channel, you can customize words that trigger mention notifications in **Account Settings** > **Notifications** > **Words that trigger mentions**. By default, you will receive mention notifications on your first name, and you can add more words by typing them into the input box separated by commas. This is useful if you want to be notified of all posts on certain topics, for example, “interviewing” or “marketing”.

## Recent Mentions
Click `@` next to the search box to query for your most recent @mentions and words that trigger mentions. Click **Jump** next to a search result in the RHS to jump the center pane to the channel and location of the message with the mention.
