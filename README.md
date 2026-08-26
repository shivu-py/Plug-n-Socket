# We will use this readme to communicate here about the ideas/plans, and changes we make

## QUERIES:
- Questions to be asked under this section
   
## ToDo (PRIORITY WISE):
- Add the User profiling section
- Add the Feed section GET method to load the recent posts
- Adding the ranking algorithm to show user interest 80% and rest 20% random posts
- Interacting with the random post will also involve in calculating the ranking of interest to be shown to user

## Done:
- I have removed the "Thought" model as we discussed yesterday, we will first do the "Talks" part then we will see what else we can add
- Added the Authentication of Register/Login with the JWT session token with the token expire time of 60 Min
- Added the User Post and the Sub post (POST method) having the endpoint **/new_post** and **/sub_post**

## Endpoint Working:
- **new_post** requires formdata -
   - content_type -> Image , Video , Text 
   - post_type -> main
   - content -> "Why Chernobyl Happened ?"
   - caption -> "they no proper work , reactor kaboom. All vaporise like bomboclaat"
   - mediafile -> Image File or Video File (limited extensions only) (OPTIONAL)
   - parent_post_id -> must be empty

- **sub_post** requires formdata -
   - content_type -> Image , Video , Text 
   - post_type -> must be subpost or reply
   - content -> "Chernobyl Kaboom how killed ?"
   - caption -> "again they no proper work , reactor kaboom. All vaporise like bomboclaat"
   - mediafile -> Image File or Video File (limited extensions only) (OPTIONAL)
   - parent_post_id -> Important
