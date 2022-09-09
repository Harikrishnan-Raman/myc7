from rest_framework import serializers
from .models import projectDatabase, assignmentDatabase, studentDatabase, evaluationDatabase, \
    submissionDatabase, instructorDatabase


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectDatabase
        fields = ('courseInstructor', 'courseName', 'courseDescription', 'courseCode', 'courseStartDate', 'courseEndDate', 'assignmentQuantity')


#       {"courseInstructor": "abc", "courseName": "capstone", "courseDescription": "this is capstone course",
#         "courseCode": "CFSEC1", "courseStartDate": DD / MM / YYYY, "courseEndDate": DD / MM / YYYY,
#         "assignmentQuantity": 2}}      fields = ('projName', 'projDescription', 'projCode', 'projInstructor', 'projNumAssignment')

#"courseStartDate": DD / MM / YYYY, "courseEndDate": DD / MM / YYYY,

class assignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignmentDatabase
        fields = ('assignmentName', 'assignmentDescription', 'assignmentDueDate', 'assignmentCode',
                  'assignmentRequiresGit', 'assignmentDocument', 'assignmentMarksTotal', 'assignmentMarksSplit1',
                  'assignmentMarksSplit2', 'assignmentMarksSplit3', 'assignmentMarksSplit4')



class instructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = instructorDatabase
        fields = ('projCode', 'projInstructor', 'universityID')


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentDatabase
        fields = ('studentName', 'universityID', 'studentGroupNum')


class submissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = submissionDatabase
        fields = ('submissionDocument', 'submissionGitURL', 'universityID')


class evaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = evaluationDatabase
        fields = ('assignmentCode', 'universityID', 'studentMarksSplit1', 'studentMarksSplit2',
                  'studentMarksSplit3', 'studentMarksSplit4', 'studentMarksTotal')
