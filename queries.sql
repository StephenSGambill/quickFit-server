DELETE FROM auth_user
WHERE id =2

UPDATE auth_user
SET is_staff = True
WHERE id = 3


DELETE FROM qfsapi_workoutexercise;
DELETE FROM qfsapi_workout;
DELETE FROM qfsapi_exercise;
DELETE FROM qfsapi_completedworkout;

DELETE FROM auth_user
DELETE FROM authtoken_token
DELETE FROM qfsapi_member
DELETE FROM qfsapi_completedworkout
DELETE FROM qfsapi_exercise
DELETE FROM qfsapi_workoutexercise



UPDATE qfsapi_completedworkout
SET member_id = 1
WHERE id = 3


