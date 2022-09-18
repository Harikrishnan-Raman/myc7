from rest_framework import serializers
from .models import projectDatabase, assignmentDatabase, evaluationDatabase, marksSplitDatabase, marksDatabase


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectDatabase
        fields = ('pk', 'courseInstructor', 'courseName', 'courseDescription', 'courseStartDate', 'courseEndDate', 'assignmentQuantity')




class evaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = evaluationDatabase
        fields = ('splitUpComponent', 'alottedMarks')


class assignmentSerializer(serializers.ModelSerializer):
    evaluation = evaluationSerializer(many=True)

    def create(self, validated_data):
      temp_eval_details= validated_data.pop('evaluation')
      evaludation_data = assignmentDatabase.objects.create(**validated_data)
      for i in temp_eval_details:
          evaluationDatabase.objects.create(evaludation_data=evaludation_data, **i,)
      return evaludation_data

    class Meta:
        model = assignmentDatabase
        fields = ('pk', 'projCode', 'assignmentName', 'assignmentDescription', 'assignmentStartDate', 'assignmentDueDate',
                  'assignmentRequiresGit', 'assignmentMarksTotal', 'evaluation')

    def update(self, instance, validated_data):
        evaludation_data = validated_data.pop('evaluation')
        evaluation = (instance.evaluation).all()
        evaluation = list(evaluation)
        instance.projCode = validated_data.get('projCode', instance.projCode)
        instance.assignmentName = validated_data.get('assignmentName', instance.assignmentName)
        instance.assignmentDescription = validated_data.get('assignmentDescription', instance.assignmentDescription)
        instance.assignmentStartDate = validated_data.get('assignmentStartDate', instance.assignmentStartDate)
        instance.assignmentDueDate = validated_data.get('assignmentDueDate', instance.assignmentDueDate)
        instance.assignmentRequiresGit = validated_data.get('assignmentRequiresGit', instance.assignmentRequiresGit)
        instance.assignmentMarksTotal = validated_data.get('assignmentMarksTotal', instance.assignmentMarksTotal)
        instance.save()

        for evaludation_data_i in evaludation_data:
            splitup = evaluation.pop(0)
            splitup.splitUpComponent = evaludation_data_i.get('splitUpComponent', splitup.splitUpComponent)
            splitup.alottedMarks = evaludation_data_i.get('alottedMarks', splitup.alottedMarks)
            splitup.save()
        return instance




class marksSplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = marksSplitDatabase
        fields = ('obtainedMarks', 'alottedMarks')


class marksSerializer(serializers.ModelSerializer):
    eval = marksSplitSerializer(many=True)

    def create(self, validated_data):
      temp_details= validated_data.pop('eval')
      eval_data = marksDatabase.objects.create(**validated_data)
      for i in temp_details:
          marksSplitDatabase.objects.create(eval_data=eval_data, **i,)
      return eval_data

    class Meta:
        model = marksDatabase
        fields = ('pk', 'assignmentCode', 'groupID', 'comment', 'eval')

    def update(self, instance, validated_data):
        eval_data = validated_data.pop('eval')
        eval = (instance.eval).all()
        eval = list(eval)
        instance.assignmentCode = validated_data.get('assignmentCode', instance.assignmentCode)
        instance.groupID = validated_data.get('groupID', instance.groupID)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()

        for eval_data_i in eval_data:
            evalt = eval.pop(0)
            evalt.obtainedMarks = eval_data_i.get('obtainedMarks', evalt.obtainedMarks)
            evalt.alottedMarks = eval_data_i.get('alottedMarks', evalt.alottedMarks)
            evalt.save()
        return instance


