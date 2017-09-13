#!/usr/bin/env groovy
pipeline{
	agent any
	stages{
		stage('Example 1'){
			steps{
				bat 'python ./test_one.py'
			}
		}
		stage('Example 2'){
			steps{
				bat 'python ./test_two.py'
			}
		}
		stage('Example 3'){
			steps{
				bat 'python ./test_three.py'
			}
		}
	}
}